from pydantic import BaseModel
from typing import Any, Dict, List, Optional

class LoginModel(BaseModel):
    field: str
    password: str
    
    class Config:
        orm_mode = True

class RegisterModel(BaseModel):
    role: int
    username: str
    email: str
    password: str
    
    class Config:
        orm_mode = True
    

class UserAuthModel(BaseModel):
    access_token: Optional[str] = None
    id: int
    username: str
    email: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    role: int
    
    class Config:
        orm_mode = True

class AuthResponseModel(BaseModel):
    status: bool
    message: str
    data: Optional[UserAuthModel] = None
    
    class Config:
        orm_mode = True

class UpdateAdminModel(BaseModel):
    first_name: Optional[str] = None
    other_name: Optional[str] = None
    last_name: Optional[str] = None
    status: Optional[int] = None
    
    class Config:
        orm_mode = True

class UpdateAdminPasswordModel(BaseModel):
    password: str
    password_confirmation: str
    old_password: str
    
    class Config:
        orm_mode = True
