schema = { 
        "$jsonSchema": {
            "bsonType": "object",
            "required": [ "note", "avis", "avancement", "date_saisie"],
            "properties": {
                # "_id": "ObjectId",
                "eleve_id": "ObjectId",
                "trimestre_id": "ObjectId",
                "classe_id": "ObjectId",
                "matiere_id": "ObjectId",
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