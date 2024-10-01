import os
from pymongo import MongoClient
from pymongo.database import Database as PyMongoDatabase

from models.student import schema as student_schema
from models.teacher import schema as teacher_schema
from models.class_ import schema as class_schema
from models.grade import schema as grade_schema
from models.subject import schema as subject_schema
from models.trimester import schema as trimester_schema


class Database:
    _instance: "Database" = None
    client: MongoClient = None
    db: PyMongoDatabase = None

    # db settings
    user: str = os.getenv("MONGODB_INITDB_ROOT_USERNAME")
    password: str = os.getenv("MONGODB_INITDB_ROOT_PASSWORD")
    host: str = "mongodb"
    name: str = "digi-school"
    port: int = 27017
    auth_source: str = "admin"

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls)
            uri = f"mongodb://{cls.user}:{cls.password}@{cls.host}:{cls.port}?authSource={cls.auth_source}"

            cls._instance.client = MongoClient(uri)

            cls._instance.db = cls._instance.client[cls.name]
            Database.init_db()

        return cls._instance

    @staticmethod
    def get_db() -> PyMongoDatabase:
        try:
            if Database._instance is None:
                Database()

            return Database._instance.db
        except Exception as e:
            print(e)

    @staticmethod
    def init_db():
        db = Database._instance.db
        collections = [
            "student",
            "teacher",
            "class",
            "subject",
            # "grade",
            "trimester",
        ]
        validators = {
            "student": student_schema,
            "teacher": teacher_schema,
            "class": class_schema,
            "subject": subject_schema,
            # "grade": grade_schema,
            "trimester": trimester_schema,
        }

        existing_collections = db.list_collection_names()
        for collection in collections:
            if collection not in existing_collections:
                db.create_collection(collection, validator=validators[collection])
            else:
                Database.update_validator(collection, validators[collection])

        # launch csv script
        # only process if we haven't alredy by checking if the text file exists

        from utils.csv_parser import main as csv_parser

        print("Processing data")
        if os.path.exists("config/processed.txt") is False:
            print("Inserting data")
            csv_parser()
        else:
            print("Data already processed")

    @staticmethod
    def update_validator(collection_name, validator):
        command = {"collMod": collection_name, "validator": validator}
        Database._instance.db.command(command)
