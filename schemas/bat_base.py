from pydantic import BaseModel
from typing import Any, Dict, List, Optional
from datetime import datetime

class CreateBatteryModel(BaseModel):
    control_box_id: int
    state_of_charge: Optional[str] = None
    current_drawn: Optional[str] = None
    voltage: Optional[str] = None
    capacity: Optional[str] = None
    
    class Config:
        orm_mode = True

class UpdateBatteryModel(BaseModel):
    state_of_charge: Optional[str] = None
    current_drawn: Optional[str] = None
    voltage: Optional[str] = None
    capacity: Optional[str] = None
    status: Optional[int] = None
    
    class Config:
        orm_mode = True

class BatteryModel(BaseModel):
    id: int
    control_box_id: int
    reference: str
    state_of_charge: Optional[str] = None
    current_drawn: Optional[str] = None
    voltage: Optional[str] = None
    capacity: Optional[str] = None
    status: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    
    class Config:
        orm_mode = True

class BatteryResponseModel(BaseModel):
    status: bool
    message: str
    data: Optional[BatteryModel] = None

    class Config:
        orm_mode = True