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
def setup_student(function):
    # Setup code
    logging.info("Setting up test student")
    collection.delete_many({"_id": test_student.id})
    collection.insert_one(test_student.model_dump(by_alias=True))


def teardown_student(function):
    logging.info("Cleaning up test student")
    clean()


def clean():
    collection.delete_many({"_id": test_student.id})


# Tests


def test_get_students():
    response = client.get("/students/")

    assert response.status_code == 200


def test_create_student():
    clean()

    t_s = StudentCreate(
        **test_student.model_dump(by_alias=True, exclude=["id"]),
    )
    req_data = jsonable_encoder(t_s.model_dump(by_alias=True))
    print(req_data)
    logging.info(f"Request data: {req_data}")
    response = client.post(
        "/students/",
        json=req_data,
    )
    print(response.json())
    student = StudentBase(**response.json())

    assert response.status_code == 201
    assert student == t_s


def test_update_student():
    original_student = test_student
    updated_model = original_student.model_copy(update={"original_id": 888})
    req_data = jsonable_encoder(updated_model)
    logging.info(f"Sending data: {req_data}")
    response = client.patch(
        f"/students/{original_student.id}",
        json=req_data,
    )

    response_student = StudentBase(**response.json())
    logging.info(f"Response data: {response_student}")

    assert response.status_code == 200
    assert response_student.original_id == updated_model.original_id


def test_delete_student():
    response = client.delete(f"/students/{test_student.id}")
    assert response.status_code == 200
    assert response.json() == {"message": "Student deleted successfully"}
    assert collection.find_one({"_id": test_student.id}) == None
    clean()
    logging.info("Student deleted successfully")
