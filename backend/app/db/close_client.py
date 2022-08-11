from app.db.init_client import client

def closeDB():
    client.close()