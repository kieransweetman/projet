subject_schema = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["nom"],
        "properties": {
            # "_id" : "ObjectId",
            "nom": {
                "bsonType": "string",
                "description": "must be a string and is required",
            }
        },
    }
}
