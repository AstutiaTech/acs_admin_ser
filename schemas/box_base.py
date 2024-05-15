from pydantic import BaseModel
from typing import Any, Dict, List, Optional
from datetime import datetime

class CreateControlBoxModel(BaseModel):
    asset_id: int
    private_key: str
    comms_sim_card_value: Optional[str] = None
    comms_sim_card_number: Optional[str] = None
    comms_wifi_provider: Optional[str] = None
    
    class Config:
        orm_mode = True

class UpdateControlBoxModel(BaseModel):
    comms_sim_card_value: Optional[str] = None
    comms_sim_card_number: Optional[str] = None
    comms_wifi_provider: Optional[str] = None
    status: Optional[int] = 0
    
    class Config:
        orm_mode = True

class ControlBoxModel(BaseModel):
    id: int
    asset_id: int
    reference: str
    private_key: str
    comms_sim_card_value: Optional[str] = None
    comms_sim_card_number: Optional[str] = None
    comms_wifi_provider: Optional[str] = None
    status: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    
    class Config:
        orm_mode = True

class ControlBoxResponseModel(BaseModel):
    status: bool
    message: str
    data: Optional[ControlBoxModel] = None

    class Config:
        orm_mode = True
