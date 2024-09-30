from fastapi.testclient import TestClient
from fastapi.encoders import jsonable_encoder

from schemas.student_base import StudentBase, StudentCreate, StudentUpdate

from main import app

from bson import ObjectId

client = TestClient(app)

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

# Tests


def test_get_students():
    response = client.get("/students/")

    assert response.status_code == 200


def test_create_student():

    req_data = jsonable_encoder(test_student)
    print(req_data)
    response = client.post(
        "/students/",
        json=jsonable_encoder(test_student),
    )
    print("rep", response.json())
    student = StudentBase(**response.json())
    model = StudentBase(**student_data)

    assert response.status_code == 201
    assert student == model
