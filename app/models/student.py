schema = {"$jsonSchema": {
            "bsonType": "object",
            "required": [ "last_name", "name", "birth_date", "address", "sex" ],
            "properties": {
                "_id": { "bsonType": "objectId" },
                "last_name": {
                    "bsonType": "string",
                    "description" : "must be a string and is required"
                },
                "name": {
                    "bsonType": "string",
                    "description" : "must be a string and is required"
                },
                "birth_date": {
                    "bsonType": "string",
                    "description" : "must be a string and is required"
                },
                "address": {
                    "bsonType": "object",
                    # "required": [ "code_postal" ],
                    "properties": {
                        "street": { "bsonType": "string" },
                        "code_postal": { "bsonType": "string" }   
                    }
                },
                "sex": {
                    "bsonType": "string",
                    "description" : "must be a string and is required"
                },
                "class": {
                    "bsonType": "object",
                    # "required": [ "note" ],
                    "properties": {
                        "_id": { "bsonType": "objectId" },  
                    },
                    "grade": {
                        {
                            "bsonType": "object",

                            "properties": {
                                "_id": { "bsonType": "objectId" },  
                            },
                            
                            "trimester": {
                                "bsonType": "object",

                                "properties": {
                                    "_id": { "bsonType": "objectId" },  
                                }
                            },
                            "note": "int"
                        }
                    },
                },
            },
        },
}

