import os
import csv
from pymongo.database import Collection, Database as PyMongoDatabase
from bson import ObjectId
from schemas.teacher_base import TeacherBase
from datetime import datetime


def parse_student(line, db: PyMongoDatabase = None):
    return {
        "nom": line[1],
        "prenom": line[2],
        "date_naissance": line[4],
        "sexe": line[5],
        "adresse": line[6],
        "original_id": int(line[0]),
    }


def parse_teacher(line, db: PyMongoDatabase = None):
    return {
        "nom": line[1],
        "prenom": line[2],
        "date_naissance": line[3],
        "sexe": line[4],
        "adresse": line[5],
        "original_id": int(line[0]),
    }


def parse_class(line, db: PyMongoDatabase = None):
    teacher = db["teacher"].find_one({"original_id": int(line[2])})
    id = teacher["_id"]
    return {"nom": line[1], "teacher": ObjectId(id)}


def parse_subject(line, db: PyMongoDatabase = None):
    return {
        "nom": line[1],
    }


def parse_grade(line, db: PyMongoDatabase = None):
    date_saisie_string = line[1]
    date = datetime.strptime(date_saisie_string, "%Y-%m-%d %H:%M:%S.%f")
    return {
        "date_saisie": date,
        "original_id": int(line[0]),
        "note": float(line[7]),
        "avis": line[8],
        "avancement": line[9],
    }


def parse_trimester(line, db: PyMongoDatabase = None):
    return {
        "nom": line[1],
        "date": line[2],
    }


csvs = [
    {"name": "teacher.csv", "process": parse_teacher},
    {"name": "student.csv", "process": parse_student},
    {"name": "class.csv", "process": parse_class},
    {"name": "subject.csv", "process": parse_subject},
    {"name": "trimester.csv", "process": parse_trimester},
    {"name": "grade.csv", "process": parse_grade},
]


def main():
    csv_dir = "config/csv"
    from config.database import Database

    db = Database.get_db()

    for file_obj in csvs:
        file_name = file_obj["name"]
        name = file_name.split(".")[0]
        process = file_obj["process"]
        collection: Collection = db[name]

        if process is None:
            continue

        with open(os.path.join(csv_dir, file_name), "r") as f:
            reader = csv.reader(f)

            # skip head
            next(reader)

            try:
                for line in reader:
                    model = process(line, db)
                    collection.insert_one(model)
            except Exception as e:
                raise RuntimeError(f"Error while parsing {file_name}: {e}")
