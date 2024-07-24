from pydantic import BaseModel
from typing import Any, Dict, List, Optional
from datetime import datetime

class CreateRoomTypeModel(BaseModel):
    asset_type_id: int
    name: str
    description: Optional[str] = None
    file_url: str
    value_code: str
    
    class Config:
        orm_mode = True

class CreateRoomModel(BaseModel):
    asset_id: int
    room_type_id: int
    control_box_id: int
    name: str
    description: Optional[str] = None
    
    class Config:
        orm_mode = True

class UpdateRoomTypeModel(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    file_url: Optional[str] = None
    value_code: Optional[str] = None
    status: Optional[int] = None
    
    class Config:
        orm_mode = True

class UpdateRoomModel(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[int] = None
    
    class Config:
        orm_mode = True

class RoomTypeModel(BaseModel):
    id: int
    name: Optional[str] = None
    description: Optional[str] = None
    file_url: Optional[str] = None
    slug: Optional[str] = None
    value_code: Optional[str] = None
    status: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    
    class Config:
        orm_mode = True

class RoomModel(BaseModel):
    id: int
    asset_id: Optional[int] = None
    room_type_id: Optional[int] = None
    control_box_id: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    
    class Config:
        orm_mode = True

class RoomTypeResponseModel(BaseModel):
    status: bool
    message: str
    data: Optional[RoomTypeModel] = None

    class Config:
        orm_mode = True
        
class RoomResponseModel(BaseModel):
    status: bool
    message: str
    data: Optional[RoomModel] = None

    class Config:
        orm_mode = True
