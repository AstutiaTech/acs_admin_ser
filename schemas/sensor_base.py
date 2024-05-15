from pydantic import BaseModel
from typing import Any, Dict, List, Optional
from datetime import datetime

class CreateSensorModel(BaseModel):
    control_box_id: int
    sensor_type: int
    voltage_input: Optional[str] = None
    voltage_output: Optional[str] = None
    
    class Config:
        orm_mode = True

class UpdateSensorModel(BaseModel):
    voltage_input: Optional[str] = None
    voltage_output: Optional[str] = None
    status: Optional[int] = None
    
    class Config:
        orm_mode = True

class SensorModel(BaseModel):
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

class SensorResponseModel(BaseModel):
    status: bool
    message: str
    data: Optional[SensorModel] = None

    class Config:
        orm_mode = True