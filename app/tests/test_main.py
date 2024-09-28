from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}


def test_read_students():
    response = client.get("/students/")
    assert response.status_code == 200
    assert response.json() == []


def test_create_student():
    student = {
        "nom": "Doe",
        "prenom": "John",
        "age": 20,
        "sexe": "M",
        "adresse": "123 rue de la torche",
    }
    response = client.post(
        "/students/",
        json=student,
    )
    assert response.status_code == 200
    assert response.json() == {}
