schema = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["name"],
        "properties": {
            "_id": {"bsonType": "objectId"},
            "name": {
                "bsonType": "string",
                "description": "must be a string and is required",
            },
            "teacher": {
                "bsonType": "object",
                "properties": {
                    "_id": {"bsonType": "objectId"},
                },
            },
            "students": {
                "bsonType": "array",
                "items": {
                    "bsonType": "object",
                    "required": ["_id", "name"],
                    "properties": {
                        "_id": {"bsonType": "objectId"},
                        "name": {"bsonType": "string"},
                    },
                },
            },
        },
    }
}
