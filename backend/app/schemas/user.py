from pydantic import BaseModel, EmailStr

class User(BaseModel):
    id: str
    email: EmailStr
    passwordHash: str
    token: str
    firstName: str
    lastName: str