from wsgiref.validate import validator
from pymongo import MongoClient

# Créer une instance de connexion MongoDB
client = MongoClient('mongodb://localhost:27017/')
# Sélectionner une base de données
db = client['digischool']
#collection=db['movies']

db.create_collection(
    'eleve',
    validator={ 
        "$jsonSchema": {
            "bsonType": "object",
            "properties": {
                "nom": {
                },
                "prenom": {
                },
                "classe": {
                },
                "date_naissance": {
                },
                "adresse": {
                },
                "sexe": {
                },
            },
        },
    })

collection=db['eleve']

db.create_collection(
    'prof',
    validator={ 
        "$jsonSchema": {
            "bsonType": "object",
            "properties": {
                "nom": {
                },
                "prenom": {
                },
                "date_naissance": {
                },
                "adresse": {
                },
                "sexe": {
                },
            },
        },
    })

collection=db['prof']

db.create_collection(
    'classe',
    validator={ 
        "$jsonSchema": {
            "bsonType": "object",
            "properties": {
                "nom": {
                },
                "prof": {
                },
            }
        }
    }
)

collection=db['classe']

db.create_collection(
    'matiere',
    validator={ 
        "$jsonSchema": {
            "bsonType": "object",
            "properties": {
                "nom": {
                }
            }
        }
    }
)

collection=db['matiere']

db.create_collection(
    'trimestre',
    validator={ 
        "$jsonSchema": {
            "bsonType": "object",
            "properties": {
                "nom": {
                },
                "date": {
                    
                }
            }
        }
    }
)

collection=db['trimestre']

db.create_collection(
    'notes',
    validator={ 
        "$jsonSchema": {
            "bsonType": "object",
            "properties": {
                "date_saisie": {
                },
                "note": {
                },
                "avis": {
                },
                "avancement": {
                }
                
            }
        }
    }
)

collection=db['notes']