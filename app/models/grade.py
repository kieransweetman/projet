grade_schema = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["note", "avis", "avancement", "date_saisie"],
        "properties": {
            # "_id": "ObjectId",
            "student_id": {
                "bsonType": "objectId",
                "description": "must be an ObjectId and is required",
                "properties": {
                    "_id": {"bsonType": "objectId"},
                },
            },
            "trimestre_id": {
                "bsonType": "objectId",
                "description": "must be an ObjectId and is required",
                "properties": {
                    "_id": {"bsonType": "objectId"},
                },
            },
            "classe_id": {
                "bsonType": "objectId",
                "description": "must be an ObjectId and is required",
                "properties": {
                    "_id": {"bsonType": "objectId"},
                },
            },
            "matiere_id": {
                "bsonType": "objectId",
                "description": "must be an ObjectId and is required",
                "properties": {
                    "_id": {"bsonType": "objectId"},
                },
            },
            "note": {
                "bsonType": "double",
                "description": "must be an int and is required",
            },
            "avis": {
                "bsonType": "string",
                "description": "must be a string and is required",
            },
            "avancement": {
                "bsonType": "double",
                "description": "must be a string and is required",
            },
            "date_saisie": {
                "bsonType": "date",
                "description": "must be a string and is required",
            },
        },
    }
}
