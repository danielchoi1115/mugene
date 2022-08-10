from init_db import client

def closeDB():
    client.close()