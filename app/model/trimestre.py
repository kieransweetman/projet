schema = { 
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["nom", "date"],
            "properties": {
                "nom": {
                    "bsonType": "string",
                    "description" : "must be a string and is required" 
                },
                "date": {
                    "bsonType": "string",
                    "description" : "must be a string and is required"
                }
            }
        }
    }