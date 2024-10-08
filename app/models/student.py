schema = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["last_name", "name", "birth_date", "address", "sex"],
        "properties": {
            "_id": {"bsonType": "objectId"},
            "name": {
                "bsonType": "string",
                "description": "must be",
            },
            "last_name": {
                "bsonType": "string",
                "description": "must be a string and is required",
            },
            "birth_date": {
                "bsonType": "date",
                "description": "must be a date and is required",
            },
            "sex": {
                "bsonType": "string",
                "description": "must be a string and is required",
            },
            "address": {
                "bsonType": "string",
                "description": "must be a string and is required",
            },
            "origin_class_id": {"bsonType": "int"},
            "grades": {
                "bsonType": "array",
                "items": {
                    "bsonType": "object",
                    "properties": {
                        "_id": {"bsonType": "objectId"},
                        "subject": {"bsonType": "string"},
                        "value": {"bsonType": "double"},
                        "trimester": {
                            "bsonType": "object",
                            "properties": {
                                "_id": {"bsonType": "objectId"},
                                "name": {"bsonType": "string"},
                            },
                        },
                    },
                },
            },
        },
    },
}
