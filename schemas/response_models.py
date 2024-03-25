from pydantic import BaseModel
from typing import Any, Dict, List, Optional

class ResponseModel(BaseModel):
    status: bool
    message: str
    response_code: Optional[str] = None
    
    class Config:
        orm_mode = True
        
class ResponseDataModel(BaseModel):
    status: bool
    message: str
    data: Dict[str, Any] = None
    
    class Config:
        orm_mode = True
        
class ResponseDataListModel(BaseModel):
    status: bool
    message: str
    data: List[Any] = None
    
    class Config:
        orm_mode = True
        