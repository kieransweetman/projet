from fastapi.testclient import TestClient
import pytest
from fastapi.encoders import jsonable_encoder
import logging
from schemas.student_base import StudentBase, StudentCreate, StudentUpdate

from main import app
from config.database import Database
from utils.common import COLLECTION
from bson import ObjectId

client = TestClient(app)
db = Database().get_db()
collection = db.get_collection(COLLECTION.STUDENT.value)

## student obj model
student_data = {
    "_id": ObjectId("60f1b9b3b3b3b3b3b3b3b3b3"),
    "last_name": "Doe",
    "name": "John",
    "birth_date": "2000-01-01",
    "sex": "M",
    "address": "123 rue de la torche",
    "original_id": 777,
}
test_student = StudentBase(**student_data)

# test configs


# Fixture for setup and teardown
@pytest.fixture(scope="function")
def setup_student():
    # Setup code
    clean()
    id = collection.insert_one(
        {
            "_id": ObjectId(test_student.id),
            "last_name": test_student.last_name,
            "name": test_student.name,
            "birth_date": test_student.birth_date,
            "sex": test_student.sex,
            "address": test_student.address,
            "original_id": test_student.original_id,
        }
    ).inserted_id
    logging.info(f"Inserted student with id: {id}")
    yield
    # Teardown code
    logging.info("Cleaning up test student")
    clean()


def clean():
    count = collection.delete_many({"_id": ObjectId(test_student.id)})
    logging.info(f"Deleted {count.deleted_count} student(s)")


# Tests


def test_get_students():
    response = client.get("/students/")

    assert response.status_code == 200


@pytest.mark.usefixtures("setup_student")
def test_create_student():
    clean()

    t_s = StudentCreate(
        **test_student.model_dump(by_alias=True, exclude=["id"]),
    )
    req_data = jsonable_encoder(t_s.model_dump(by_alias=True))
    logging.info(f"Request data: {req_data}")
    response = client.post(
        "/students/",
        json=req_data,
    )

    student_data = response.json()

    assert response.status_code == 201
    assert student_data["original_id"] == t_s.original_id


@pytest.mark.usefixtures("setup_student")
def test_update_student():
    req_data = {"original_id": 888}
    logging.info(f"Sending data: {req_data}")
    response = client.patch(
        f"/students/{test_student.id}",
        json=req_data,
    )

    response_student = response.json()
    logging.info(f"Response data: {response_student}")
    print(response_student)
    assert response.status_code == 200
    assert response_student["original_id"] == req_data["original_id"]


def test_delete_student():
    response = client.delete(f"/students/{test_student.id}")
    assert response.status_code == 204
    assert collection.find_one({"_id": test_student.id}) == None
    clean()
    logging.info("Student deleted successfully")
