from pydantic import BaseModel
from typing import Any, Dict, List, Optional
from datetime import datetime

class CreatePortTypeModel(BaseModel):
    name: str
    description: Optional[str] = None
    file_url: str
    value_code: str
    
    class Config:
        orm_mode = True

class CreatePortModel(BaseModel):
    room_id: int
    control_box_id: int
    port_type_id: int
    appliance_name: Optional[str] = None
    room_name: Optional[str] = None
    power_rating: Optional[str] = None
    current_drawn: Optional[str] = None
    priority_status: Optional[int] = 0
    
    class Config:
        orm_mode = True

class UpdatePortTypeModel(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    file_url: Optional[str] = None
    value_code: Optional[str] = None
    status: Optional[int] = None
    
    class Config:
        orm_mode = True

class UpdatePortModel(BaseModel):
    appliance_name: Optional[str] = None
    room_name: Optional[str] = None
    power_rating: Optional[str] = None
    current_drawn: Optional[str] = None
    priority_status: Optional[int] = None
    status: Optional[int] = None
    
    class Config:
        orm_mode = True

class PortTypeModel(BaseModel):
    id: int
    name: Optional[str] = None
    description: Optional[str] = None
    file_url: Optional[str] = None
    value_code: Optional[str] = None
    status: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    
    class Config:
        orm_mode = True


class PortModel(BaseModel):
    id: int
    control_box_id: int
    reference: str
    appliance_name: Optional[str] = None
    room_name: Optional[str] = None
    power_rating: Optional[str] = None
    current_drawn: Optional[str] = None
    priority_status: Optional[int] = None
    status: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    
    class Config:
        orm_mode = True

class PortTypeResponseModel(BaseModel):
    status: bool
    message: str
    data: Optional[PortTypeModel] = None

    class Config:
        orm_mode = True
        
class PortResponseModel(BaseModel):
    status: bool
    message: str
    data: Optional[PortModel] = None

    class Config:
        orm_mode = True