class UserDB:
    DB = 'user_db'
    COLLECTION = 'users'

class BlockDB:
    DB = 'storage_db'
    COLLECTION = 'storages'

class WorkSpaceDB:
    DB = 'storage_db'
    COLLECTION = 'storages'
    
userdb_config = UserDB()
blockdb_config = BlockDB()
workdb_config = WorkSpaceDB()