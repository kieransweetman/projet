from fastapi.testclient import TestClient
from schemas.student_base import StudentBase
from datetime import datetime
from config.database import Database

from main import app

client = TestClient(app)


def test_read_students():
    response = client.get("/students/")
    assert response.status_code == 200


## student tests
student_data = {
    "nom": "Doe",
    "prenom": "John",
    "date_naissance": "2000-01-01",
    "sexe": "M",
    "adresse": "123 rue de la torche",
    "original_id": 777,
}


def clean_student_data():
    student = StudentBase(**student_data)

    db = Database().get_db()
    db["students"].delete_one({"original_id": student.original_id})


def test_create_student():

    response = client.post(
        "/students/",
        json=student_data,
    )

    student = StudentBase(**response.json())
    model = StudentBase(**student_data)

    assert response.status_code == 201
    assert student.model_dump(exclude="id") == model.model_dump(exclude="id")
    clean_student_data()


def test_get_student():
    response = client.post(
        "/students/",
        json=student_data,
    )

    created_student_data = response.json()
    print("created_student_data", created_student_data)
    student = StudentBase(**created_student_data)
    response = client.get(f"/students/{student.id}")

    assert response.status_code == 200
    clean_student_data()


def test_delete_student():
    response = client.post(
        "/students/",
        json=student_data,
    )

    created_student_data = response.json()

    student = StudentBase(**created_student_data)

    response = client.delete(f"/students/{student.id}")
    assert response.status_code == 204
    clean_student_data()
