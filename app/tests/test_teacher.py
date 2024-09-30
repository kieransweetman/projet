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
def setup_teacher(function):
    # Setup code
    logging.info("Setting up test teacher")
    collection.delete_many({"_id": test_teacher.id})
    collection.insert_one(test_teacher.model_dump(by_alias=True))


def teardown_teacher(function):
    logging.info("Cleaning up test teacher")
    clean()


def clean():
    collection.delete_one({"_id": test_teacher.id})


# Tests


def test_get_teachers():
    response = client.get("/teachers/")

    assert response.status_code == 200


def test_create_teacher():

    req_data = jsonable_encoder(test_teacher)
    print(req_data)
    logging.info(f"Request data: {req_data}")
    response = client.post(
        "/teachers/",
        json=req_data,
    )
    teacher = TeacherBase(**response.json())

    assert response.status_code == 201
    assert teacher == test_teacher


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
