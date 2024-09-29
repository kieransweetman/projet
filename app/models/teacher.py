teacher_schema = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["nom", "prenom", "date_naissance", "sexe"],
        "properties": {
            "nom": {
                "bsonType": "string",
                "description": "must be a string and is required",
            },
            "prenom": {
                "bsonType": "string",
                "description": "must be a string and is required",
            },
            "date_naissance": {
                "bsonType": "date",
                "description": "must be a date and is required",
            },
            "adresse": {
                "bsonType": "string",
            },
            "sexe": {
                "bsonType": "string",
                "description": "must be a string and is required",
            },
            "classes": {
                "bsonType": "array",
                "items": {
                    "bsonType": "object",
                    "properties": {
                        "classe_id": {"bsonType": "objectId"},
                    },
                },
            },
        },
    },
}
