# all the imports
import os
from dotenv import load_dotenv
from fastapi import FastAPI, APIRouter, HTTPException
from config.database import Database
from routes import student_router
from utils.csv_parser import main as csv_parser


# Load environment variables from .env file
load_dotenv()

app: FastAPI = FastAPI()
router = APIRouter()

# Create a connection to the database
try:
    db = Database().get_db()


except Exception as e:
    raise HTTPException(status_code=500, detail=f"Could not connect to MongoDB: {e}")


router.include_router(student_router.router)
# TODO: Add the other router files
# router.include_router(teacher.router)
# router.include_router(class.router)

app.include_router(router)
