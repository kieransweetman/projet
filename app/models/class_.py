class_schema = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["nom"],
        "properties": {
            "nom": {
                "bsonType": "string",
                "description": "must be a string and is required",
            },
            "teacher": {
                "bsonType": "object",
                "properties": {
                    "teacher_id": {"bsonType": "objectId"},
                },
            },
        },
    }
}
