# import bcrypt


# def get_password_hash(password: str) -> str:
#     hashed = bcrypt.hashpw(password, bcrypt.gensalt())
#     return hashed.decode('utf-8')


# def verify_password(plain_password: str, hashed_password: str) -> bool:
#     plain_password = plain_password.encode('utf-8')
#     return bcrypt.checkpw(plain_password, hashed_password)
from passlib.context import CryptContext


PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return PWD_CONTEXT.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return PWD_CONTEXT.hash(password)
