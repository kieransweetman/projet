schema = { 
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["name", "date"],
            "properties": {
                "_id": { "bsonType": "objectId" },
                "name": {
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