schema = {"$jsonSchema": {
            "bsonType": "object",
            "required": [ "nom", "prenom", "date_naissance", "addresse", "sexe" ],
            "properties": {
                "nom": {
                    "bsonType": "string",
                    "description" : "must be a string and is required"
                },
                "prenom": {
                    "bsonType": "string",
                    "description" : "must be a string and is required"
                },
                "date_naissance": {
                    "bsonType": "string",
                    "description" : "must be a string and is required"
                },
                "adresse": {
                    "bsonType": "object",
                    # "required": [ "code_postal" ],
                    "properties": {
                        "street": { "bsonType": "string" },
                        "code_postal": { "bsonType": "string" }   
                    }
                },
                "sexe": {
                    "bsonType": "string",
                    "description" : "must be a string and is required"
                },
                "classe": {
                    "bsonType": "object",
                    # "required": [ "note" ],
                    "classe_id" : "ObjectId",
                    "notes": [
                        {
                            "_id":"ObjectId",
                            "trimestre_id":"ObjectId",
                            "note": "int"
                        }
                    ]
                },
            },
        },
}

