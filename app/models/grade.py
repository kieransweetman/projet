schema = { 
        "$jsonSchema": {
            "bsonType": "object",
            "required": [ "value", "opinion", "advancement", "date_entered"],
            "properties": {
                "_id": { "bsonType": "objectId" },
                "student": {
                    "bsonType": "object",
                    "properties": {
                        "_id": { "bsonType": "objectId" },  
                    }
                },
                "trimester": {
                    "bsonType": "object",
                    "properties": {
                        "_id": { "bsonType": "objectId" },  
                    }
                },
                "class": {
                    "bsonType": "object",
                    "properties": {
                        "_id": { "bsonType": "objectId" },  
                    }
                },
                "subject": {
                    "bsonType": "object",
                    "properties": {
                        "_id": { "bsonType": "objectId" },  
                    }
                },
                "date_entered": {
                    "bsonType": "string",
                    "description" : "must be a string and is required"
                },
                "value": {
                    "bsonType": "double",
                    "description" : "must be an double and is required"
                },
                "opinion": {
                    "bsonType": "string",
                    "description" : "must be a string and is required"
                },
                "advancement": {
                    "bsonType": "double",
                    "description" : "must be a double and is required"
                },
            }
        }
    }