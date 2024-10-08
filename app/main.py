# all the imports
import os
from dotenv import load_dotenv
from fastapi import FastAPI, APIRouter, HTTPException
from config.database import Database
from routes import student, teacher, class_


# Load environment variables from .env file
load_dotenv()

app: FastAPI = FastAPI()
router = APIRouter()

# Create a connection to the database
try:
    db = Database().get_db()
except Exception as e:
    raise HTTPException(
        status_code=500, detail=f"\n ### \nProblem with DB setup:\n {e} \n####"
    )


router.include_router(student.router)
# TODO: Add the other router files
router.include_router(teacher.router)
router.include_router(class_.router)

app.include_router(router)


@app.get("/")
def read_root():
    try:
        return {"msg": "Hello World"}
    except Exception as e:
        print(r"{str(e)}")
        return HTTPException(status_code=500, detail=r"{str(e)}")
