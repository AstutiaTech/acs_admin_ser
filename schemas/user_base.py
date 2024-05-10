from pydantic import BaseModel
from typing import Any, Dict, List, Optional
from datetime import datetime

class CreateOwnerModel(BaseModel):
    name: str
    description: Optional[str] = None
    
    class Config:
        orm_mode = True

class UpdateOwnerModel(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[int] = None
    
    class Config:
        orm_mode = True

class OwnerModel(BaseModel):
    id: int
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[int] = None
    created_at: Optional[datetime] = None
    
    class Config:
        orm_mode = True

class OwnerResponseModel(BaseModel):
    status: bool
    message: str
    data: Optional[OwnerModel] = None

    class Config:
        orm_mode = True

class CreateUserModel(BaseModel):
    owner_id: int
    username: str
    email: str
    password: str
    role: int

    class Config:
        orm_mode = True

class UpdateUserModel(BaseModel):
    password: Optional[str] = None
    role: Optional[int] = None

    class Config:
        orm_mode = True

class UserModel(BaseModel):
    owner_id: int
    username: Optional[str] = None
    email: Optional[str] = None
    role: Optional[int] = None
    status: Optional[int] = None
    created_at: Optional[datetime] = None

    class Config:
        orm_mode = True

class UserResponseModel(BaseModel):
    status: bool
    message: str
    data: Optional[UserModel] = None

    class Config:
        orm_mode = True