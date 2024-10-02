from fastapi.testclient import TestClient
import pytest
from fastapi.encoders import jsonable_encoder
import logging
from schemas.class_base import ClassBase, ClassCreate, ClassUpdate
from schemas.student_base import StudentBase
from schemas.teacher_base import TeacherBase
from tests.test_teacher import setup_teacher
from main import app
from config.database import Database
from utils.common import COLLECTION
from bson import ObjectId
from datetime import datetime

client = TestClient(app)
db = Database().get_db()
collection = db.get_collection(COLLECTION.CLASS.value)

## class obj model
class_data = {
    "_id": ObjectId("60f1b9b3b3b3b3b3b3b3b3b3"),
    "name": "cm1",
}
test_class = ClassBase(**class_data)

# test configs


# Fixture for setup and teardown
@pytest.fixture(scope="function")
def setup_class():
    # Setup code
    clean()
    model = {
        "_id": ObjectId(test_class.id),
        "name": test_class.name,
    }
    id = collection.insert_one(model).inserted_id
    logging.info(f"Inserted class with id: {id}")
    yield model
    # Teardown code
    logging.info("Cleaning up test class")
    clean()


@pytest.fixture(scope="function")
def set_teacher():
    clean_teacher()
    model = {
        "_id": ObjectId("60f1b9b3b3b3b3b3b3b3b3b3"),
        "last_name": "Doe",
        "name": "John",
        "birth_date": datetime(2000, 1, 1),
        "sex": "M",
        "address": "123 rue de la torche",
        "original_id": 777,
    }
    try:
        id = db.get_collection(COLLECTION.TEACHER.value).insert_one(model).inserted_id
    except Exception as e:
        logging.error(f"Error: {e}")

    yield model
    clean_teacher()


@pytest.fixture(scope="function")
def set_student():
    clean_student()
    model = {
        "_id": ObjectId("60f1b9b3b3b3b3b3b3b3b3b3"),
        "last_name": "Doe",
        "name": "John",
        "address": "123 rue de la torche",
        "sex": "M",
        "birth_date": datetime(2000, 1, 1),
    }
    try:
        id = db.get_collection(COLLECTION.STUDENT.value).insert_one(model).inserted_id
    except Exception as e:
        logging.error(f"Error: {e}")

    yield model
    clean_student()


def clean_student():
    result = db.get_collection(COLLECTION.STUDENT.value).delete_many(
        {"_id": ObjectId("60f1b9b3b3b3b3b3b3b3b3b3")}
    )
    logging.info(f"Deleted teacher: {result.deleted_count}")


def clean_teacher():
    result = db.get_collection(COLLECTION.TEACHER.value).delete_many(
        {"_id": ObjectId("60f1b9b3b3b3b3b3b3b3b3b3")}
    )
    logging.info(f"Deleted teacher: {result.deleted_count}")


def clean():
    result = collection.delete_many({"_id": ObjectId(test_class.id)})
    logging.info(f"Deleted {result.deleted_count} class(s)")


# Tests


def test_get_class():
    response = client.get("/class/")

    assert response.status_code == 200


@pytest.mark.usefixtures("set_teacher")
def test_create_class(set_teacher):
    clean()

    req_data = test_class.model_dump(by_alias=True)
    logging.info(f"Request data\n: {req_data}")
    response = client.post(
        "/class/",
        json=req_data,
    )
    print(f"response: ", response.json())
    assert response.status_code == 201


def test_update_class():
    original_class = test_class
    req_data = {"name": "updated-name"}
    logging.info(f"Sending data: {req_data}")
    response = client.patch(
        f"/class/{original_class.id}",
        json=req_data,
    )

    response_class = ClassBase(**response.json())
    logging.info(f"Response data: {response_class}")

    assert response.status_code == 200
    assert response_class.name == req_data.get("name")


def test_delete_class():
    response = client.delete(f"/class/{test_class.id}")
    assert response.status_code == 200
    assert collection.find_one({"_id": test_class.id}) == None
    clean()
    logging.info("Class deleted successfully")


# @pytest.mark.usefixtures("setup_class")
# @pytest.mark.usefixtures("set_teacher")
# @pytest.mark.usefixtures("set_student")
# def test_add_student(setup_class, set_student, set_teacher):

#     teacher = TeacherBase(**set_teacher)
#     class_ = ClassBase(**setup_class)

#     class_.teacher = teacher
#     db.get_collection(COLLECTION.CLASS.value).update_one(
#         {"_id": class_.id}, {"$set": class_.model_dump(by_alias=True)}
#     )

#     student = StudentBase(**set_student)
#     req_data = [{"_id": str(student.id), "name": student.name}]

#     url = f"/class/{class_.id}/add_students"

#     response = client.patch(url, json=req_data)

#     assert response.status_code == 201
