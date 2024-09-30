schema = {"$jsonSchema": {
            "bsonType": "object",
            "required": [ "nom", "prenom", "date_naissance","sexe" ],
            "properties": {
                "lastname": {
                    "bsonType": "string",
                    "description": "must be a string and is required"
                },
                "name": {
                    "bsonType": "string",
                    "description": "must be a string and is required"
                },
                "birth_date": {
                    "bsonType": "string",
                    "description": "must be a string and is required"
                },
                "adress": {
                    "bsonType": "object",
                    "required": [ "code_postal" ],
                    "properties": {
                        "street": { "bsonType": "string" },
                        "code_postal": { "bsonType": "string" }   
                    }
                },
                "sex": {
                    "bsonType": "string",
                    "description": "must be a string and is required"
                },
                "class":[
                    {
                       "bsonType": "object",
                        "properties": {
                        "_id": { "bsonType": "objectId" },  
                        }
                    }
                ]
            },
        },
          }