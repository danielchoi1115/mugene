
from pymongo import MongoClient
from app.db.config import dbconfig


client = MongoClient(
    host=dbconfig.HOST,
    port=dbconfig.PORT,
    username=dbconfig.USERNAME,
    password=dbconfig.PASSWORD
)
