from pydantic import BaseModel
from typing import Any, Dict, List, Optional
from datetime import datetime

class CreatePortModel(BaseModel):
    control_box_id: int
    appliance_name: Optional[str] = None
    room_name: Optional[str] = None
    power_rating: Optional[str] = None
    current_drawn: Optional[str] = None
    priority_status: Optional[int] = 0
    
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

class PortResponseModel(BaseModel):
    status: bool
    message: str
    data: Optional[PortModel] = None

    class Config:
        orm_mode = True