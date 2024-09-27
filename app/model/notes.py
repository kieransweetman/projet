schema = { 
        "$jsonSchema": {
            "bsonType": "object",
            "required": [ "note", "avis", "avancement", "date_saisie"],
            "properties": {
                "note": {
                    "bsonType": "int",
                    "description" : "must be an int and is required"
                },
                "avis": {
                    "bsonType": "string",
                    "description" : "must be a string and is required"
                },
                "avancement": {
                    "bsonType": "string",
                    "description" : "must be a string and is required"
                },
                "date_saisie": {
                    "bsonType": "string",
                    "description" : "must be a string and is required"
                },
                
            }
        }
    }