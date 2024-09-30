import os
import csv
from pymongo.database import Collection, Database as PyMongoDatabase
from bson import ObjectId
from schemas.teacher_base import TeacherBase
from schemas.student_base import StudentBase
from datetime import datetime

from config.database import Database

db = Database.get_db()


def parse_student(line):
    date = datetime.strptime(line[4], "%Y-%m-%d %H:%M:%S.%f")

    student = StudentBase(
        last_name=line[1],
        name=line[2],
        birth_date=date,
        address=line[5],
        sex=line[6],
        original_id=int(line[0]),
    )

    return student.model_dump()


def parse_teacher(line):
    date = datetime.strptime(line[3], "%Y-%m-%d %H:%M:%S.%f")

    teacher = TeacherBase(
        last_name=line[1],
        name=line[2],
        birth_date=date,
        sex=line[4],
        address=line[5],
        original_id=int(line[0]),
    )

    return teacher.model_dump()


def parse_class(line):
    teacher = db["teacher"].find_one({"original_id": int(line[2])})
    id = teacher["_id"]
    return {"last_name": line[1], "teacher": {"_id": id}}


def parse_subject(line):
    return {
        "last_name": line[1],
    }


def parse_grade(line):
    date_saisie_string = line[1]
    date = datetime.strptime(date_saisie_string, "%Y-%m-%d %H:%M:%S.%f")
    return {
        "date_saisie": date,
        "note": float(line[7]),
        "avis": line[8],
        "avancement": float(line[9]),
        "original_id": int(line[0]),
    }


def parse_trimester(line):
    return {
        "last_name": line[1],
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

            print(
                "\n##################\n",
                "Processing: ",
                file_name,
                "\n##################\n",
            )

            try:
                for line in reader:
                    model = process(line)
                    collection.insert_one(model)

            except Exception as e:
                raise RuntimeError(f"Error while parsing {file_name}: {e}")

    # create a file to indicate that we have processed the csv files
    with open(os.path.join(csv_dir, "../", "processed.txt"), "a") as f:
        f.write(f"{True}")
