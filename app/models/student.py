schema = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["nom", "prenom", "date_naissance", "addresse", "sexe"],
        "properties": {
            "_id": {"bsonType": "objectId"},
            "lastname": {
                "bsonType": "string",
                "description": "must be a string and is required",
            },
        },
        "sex": {
            "bsonType": "string",
            "description": "must be a string and is required",
        },
        "class": {
            "bsonType": "object",
            # "required": [ "note" ],
            "properties": {
                "_id": {"bsonType": "objectId"},
            },
            "grade": {
                {
                    "bsonType": "object",
                    "properties": {
                        "_id": {"bsonType": "objectId"},
                    },
                    "trimester": {
                        "bsonType": "object",
                        "properties": {
                            "_id": {"bsonType": "objectId"},
                        },
                    },
                    "note": "int",
                }
            },
        },
    },
}
