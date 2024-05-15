from pydantic import BaseModel
from typing import Any, Dict, List, Optional
from datetime import datetime

class CreateInverterModel(BaseModel):
    control_box_id: int
    capacity: Optional[str] = None
    voltage_input: Optional[str] = None
    voltage_output: Optional[str] = None
    
    class Config:
        orm_mode = True

class UpdateInverterModel(BaseModel):
    capacity: Optional[str] = None
    voltage_input: Optional[str] = None
    voltage_output: Optional[str] = None
    status: Optional[int] = None
    
    class Config:
        orm_mode = True

class InverterModel(BaseModel):
    id: int
    control_box_id: int
    reference: str
    voltage_input: Optional[str] = None
    voltage_output: Optional[str] = None
    status: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    
    class Config:
        orm_mode = True
    
class InverterResponseModel(BaseModel):
    status: bool
    message: str
    data: Optional[InverterModel] = None

    class Config:
        orm_mode = True