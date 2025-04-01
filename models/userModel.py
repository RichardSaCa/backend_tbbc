from pydantic import BaseModel
from typing import List

# modelar tabla de la base de datos

class User(BaseModel):
    id: int
    name: str
    phone: str
    email: str
    
class createUser(BaseModel):
    name: str
    phone: str
    email: str
    
class Users(BaseModel):
    users: List[User]

# Modelo para actualizar   
class UpdateUser(BaseModel):
    name: str
    phone: str
    email: str