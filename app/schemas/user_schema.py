from typing import List
from pydantic import BaseModel, EmailStr
from app.schemas.role_schema import RoleRead

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserRead(BaseModel):
    id: int
    name: str
    email: EmailStr
    roles: List[RoleRead] = []

    class Config:
        orm_mode = True
