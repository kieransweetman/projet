import os
import csv
from pymongo.database import Collection


# for Student & Teacher model
def parse_student(line, db=None):
    return {
        "nom": line[1],
        "prenom": line[2],
        "date_naissance": line[4],
        "sexe": line[5],
        "adresse": line[6],
    }


def parse_teacher(line, db=None):
    return {
        "nom": line[1],
        "prenom": line[2],
        "date_naissance": line[3],
        "sexe": line[4],
        "adresse": line[5],
    }


def parse_class(line, db=None):
    return {"nom": line[1], "teacher": line[2]}


def parse_subject(line, db=None):
    return {
        "nom": line[1],
    }


def parse_grade(line, db=None):
    pass
    print("Parsing grade line:", line)


def parse_trimester(line, db=None):
    return {
        "nom": line[1],
        "date": line[2],
    }


parsing_strategies = {
    "student.csv": parse_student,
    "teacher.csv": parse_teacher,
    "class.csv": parse_class,
    "subject.csv": parse_subject,
    # "grade.csv": parse_grade,
    "trimester.csv": parse_trimester,
}


def main():
    csv_dir = "config/csv"
    from config.database import Database

    db = Database.get_db()

    for file in os.listdir(csv_dir):
        process = parsing_strategies.get(file)
        name = file.split(".")[0]
        collection: Collection = db[name]

        if process is None:
            continue

        with open(f"{csv_dir}/{file}", "r") as f:
            reader = csv.reader(f)

            # skip head
            next(reader)

            try:
                for line in reader:
                    model = process(line)
                    collection.insert_one(model)
            except Exception as e:
                raise RuntimeError(f"Error while parsing {file}: {e}")
