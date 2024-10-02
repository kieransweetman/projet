student_pipeline = [
    {
        "$lookup": {
            "from": "grade",
            "localField": "_id",
            "foreignField": "student._id",
            "as": "grades_info",
        }
    },
    {"$unwind": {"path": "$grades_info", "preserveNullAndEmptyArrays": False}},
    {
        "$lookup": {
            "from": "subject",
            "localField": "grades_info.subject._id",
            "foreignField": "_id",
            "as": "subject_info",
        }
    },
    {"$unwind": {"path": "$subject_info", "preserveNullAndEmptyArrays": True}},
    {
        "$group": {
            "_id": "$_id",
            "grades": {
                "$push": {
                    "_id": "$grades_info._id",
                    "value": "$grades_info.value",
                    "subject": "$subject_info.name",
                    "trimester": {
                        "_id": "$grades_info.trimester._id",
                        "name": "$grades_info.trimester.name",
                    },
                }
            },
        }
    },
    {
        "$merge": {
            "into": "student",
            "whenMatched": "merge",
            "whenNotMatched": "discard",
        }
    },
]

class_pipeline = [
    {
        "$lookup": {
            "from": "student",
            "localField": "original_id",
            "foreignField": "origin_class_id",
            "as": "students",
        }
    },
    {
        "$merge": {
            "into": "class",
            "whenMatched": "merge",
            "whenNotMatched": "discard",
        }
    },
]

teacher_pipeline = [
    {
        "$lookup": {
            "from": "class",
            "localField": "_id",
            "foreignField": "teacher._id",
            "as": "class_info",
        }
    },
    {"$unwind": {"path": "$class_info", "preserveNullAndEmptyArrays": True}},
    {
        "$group": {
            "_id": "$_id",
            "classes": {
                "$push": {
                    "_id": "$class_info._id",
                }
            },
        }
    },
    {
        "$merge": {
            "into": "teacher",
            "whenMatched": "merge",
            "whenNotMatched": "discard",
        }
    },
]
