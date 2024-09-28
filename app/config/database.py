import os
from pymongo import MongoClient
from pymongo.database import Database as PyMongoDatabase


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
        collections = ["student", "teacher", "class", "subject", "grade", "trimester"]

        existing_collections = db.list_collection_names()
        for collection in collections:
            if collection not in existing_collections:
                db.create_collection(collection)

        ## finish importing csv files in /csv
