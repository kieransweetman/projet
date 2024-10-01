import csv
import os
from pathlib import Path
from pymongo.database import Collection, Database as PyMongoDatabase
from schemas.teacher_base import TeacherBase, TeacherCreate
from schemas.student_base import StudentBase, StudentCreate
from schemas.class_base import ClassBase, ClassCreate
from schemas.grade_base import GradeBase, GradeCreate
from schemas.trimester_base import TrimesterBase, TrimesterCreate
from schemas.subject_base import SubjectBase, SubjectCreate
from datetime import datetime
from bson import ObjectId
from config.database import Database

db = Database.get_db()


def parse_date(date_string):
    dt = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S.%f")
    naive_dt = dt.replace(tzinfo=None)
    return naive_dt.isoformat()


def parse_student(line):
    date = parse_date(line[4])
    student = StudentCreate(
        last_name=line[1],
        name=line[2],
        birth_date=date,
        address=line[5],
        sex=line[6],
        original_id=int(line[0]),
    )

    return student.model_dump(by_alias=True, exclude=["id"])


def parse_teacher(line):
    date = parse_date(line[3])

    teacher = TeacherCreate(
        last_name=line[1],
        name=line[2],
        birth_date=date,
        sex=line[4],
        address=line[5],
        original_id=int(line[0]),
    )

    return teacher.model_dump(by_alias=True, exclude=["id"])


def parse_class(line):

    teacher = TeacherBase(**db["teacher"].find_one({"original_id": int(line[2])}))

    class_ = ClassCreate(
        name=line[1], original_id=line[0], teacher={"_id": teacher.id}, students=[]
    ).model_dump(by_alias=True, exclude=["id"])
    class_["teacher"]["_id"] = ObjectId(class_["teacher"]["_id"])
    return class_


def parse_subject(line):

    model = {
        "name": line[1],
        "original_id": int(line[0]),
    }

    subject = SubjectCreate(**model)

    return subject.model_dump(by_alias=True, exclude=["id"])


def parse_grade(line):
    date_saisie_string = line[1]
    date = parse_date(date_saisie_string)

    student_data = db["student"].find_one({"original_id": int(line[2])})
    student = StudentBase(**student_data)

    class_data = db["class"].find_one({"original_id": int(line[3])})
    class_ = ClassBase(**class_data)

    subject_data = db["subject"].find_one({"original_id": int(line[4])})
    subject = SubjectBase(**subject_data)

    teacher_data = db["teacher"].find_one({"original_id": int(line[5])})
    teacher = TeacherBase(**teacher_data)

    d = db["trimester"].find().to_list()
    trimester_data = db["trimester"].find_one({"original_id": int(line[6])})
    trimester = TrimesterBase(**trimester_data)

    model = {
        "date_entered": date,
        "value": float(line[7]),
        "class": {"_id": class_.id},
        "student": {"_id": student.id},
        "subject": {"_id": subject.id},
        "teacher": {"_id": teacher.id},
        "trimester": {"_id": trimester.id},
        "opinion": line[8],
        "advancement": float(line[9]),
        "original_id": int(line[0]),
    }

    grade = GradeCreate(**model)

    print(grade)

    return grade.model_dump(by_alias=True, exclude=["id"])


def parse_trimester(line):

    model = {
        "name": line[1],
        "date": parse_date(line[2]),
        "original_id": int(line[0]),
    }

    trimester = TrimesterCreate(**model)

    return trimester.model_dump(by_alias=True, exclude=["id"])


csvs = [
    {"name": "subject.csv", "process": parse_subject},
    {"name": "trimester.csv", "process": parse_trimester},
    {"name": "teacher.csv", "process": parse_teacher},
    {"name": "student.csv", "process": parse_student},
    {"name": "class.csv", "process": parse_class},
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
    processed_flag = Path(csv_dir).parent / "processed.txt"
    processed_flag.touch()
