schema = {
    "$jsonSchema": {
            "bsonType": "object",
            "required": [ "nom" ],
            "properties": {
                "nom": {
                    "bsonType": "string",
                    "description" : "must be a string and is required"
                },
                "prof": {
                    "prof_id": "ObjectId"
                },
                "eleve": [
                    {
                        "eleve_id": "ObjectId",
                    },
                ],
            }
        }
}

