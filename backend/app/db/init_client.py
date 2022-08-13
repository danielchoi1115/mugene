
from pymongo import MongoClient
from config import dbconfig


client = MongoClient(
    host=dbconfig.HOST,
    port=dbconfig.PORT,
    username=dbconfig.USERNAME,
    password=dbconfig.PASSWORD
)
