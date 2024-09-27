schema = { 
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["nom", "date"],
            "properties": {
                # "_id": "ObjectId",
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