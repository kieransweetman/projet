schema = { 
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["name"],
            "properties": {
                "_id": { "bsonType": "objectId" },
                "name": {
                    "bsonType": "string",
                    "description" : "must be a string and is required"
                }
            }
            
            
        }
    }
