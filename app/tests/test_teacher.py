from fastapi.testclient import TestClient
import pytest
from fastapi.encoders import jsonable_encoder
import logging
from schemas.teacher_base import TeacherBase, TeacherCreate, TeacherUpdate

from main import app
from config.database import Database
from utils.common import COLLECTION
from bson import ObjectId

client = TestClient(app)
db = Database().get_db()
collection = db.get_collection(COLLECTION.TEACHER.value)

## teacher obj model
teacher_data = {
    "_id": ObjectId("60f1b9b3b3b3b3b3b3b3b3b3"),
    "last_name": "Doe",
    "name": "John",
    "birth_date": "2000-01-01",
    "sex": "M",
    "address": "123 rue de la torche",
    "original_id": 777,
}
test_teacher = TeacherBase(**teacher_data)

# test configs


# Fixture for setup and teardown
@pytest.fixture(scope="function")
def setup_student():
    # Setup code
    clean()
    id = collection.insert_one(
        {
            "_id": ObjectId(test_teacher.id),
            "last_name": test_teacher.last_name,
            "name": test_teacher.name,
            "birth_date": test_teacher.birth_date,
            "sex": test_teacher.sex,
            "address": test_teacher.address,
            "original_id": test_teacher.original_id,
        }
    ).inserted_id
    logging.info(f"Inserted student with id: {id}")
    yield
    # Teardown code
    logging.info("Cleaning up test student")
    clean()


def clean():
    collection.delete_one({"_id": test_teacher.id})


# Tests


def test_get_teachers():
    response = client.get("/teachers/")

    assert response.status_code == 200


def test_create_teacher():

    t_t = TeacherCreate(
        **test_teacher.model_dump(by_alias=True, exclude=["id"]),
    )
    req_data = jsonable_encoder(t_t.model_dump(by_alias=True))
    logging.info(f"Request data: {req_data}")
    response = client.post(
        "/teachers/",
        json=req_data,
    )
    teacher = TeacherBase(**response.json())

    assert response.status_code == 201


def test_update_teacher():
    original_teacher = test_teacher
    updated_model = original_teacher.model_copy(update={"original_id": 888})
    req_data = jsonable_encoder(updated_model)
    logging.info(f"Sending data: {req_data}")
    response = client.patch(
        f"/teachers/{original_teacher.id}",
        json=req_data,
    )

    response_teacher = TeacherBase(**response.json())
    logging.info(f"Response data: {response_teacher}")

    assert response.status_code == 200
    assert response_teacher.original_id == updated_model.original_id


def test_delete_teacher():
    response = client.delete(f"/teachers/{test_teacher.id}")
    assert response.status_code == 200
    assert response.json() == {"message": "Teacher deleted successfully"}
    assert collection.find_one({"_id": test_teacher.id}) == None
    clean()
    logging.info("Teacher deleted successfully")
