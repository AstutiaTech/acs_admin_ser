from pydantic import BaseModel
from typing import Any, Dict, List, Optional
from datetime import datetime

class CreateAssetTypeModel(BaseModel):
    name: str
    description: Optional[str] = None
    file_url: str
    value_code: str
    
    class Config:
        orm_mode = True

class CreateAssetModel(BaseModel):
    owner_id: int
    asset_type_id: int
    name: str
    description: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    latitude: Optional[str] = None
    longitude: Optional[str] = None
    
    class Config:
        orm_mode = True

class UpdateAssetTypeModel(BaseModel):
    asset_type_id: int
    name: Optional[str] = None
    description: Optional[str] = None
    file_url: Optional[str] = None
    value_code: Optional[str] = None
    
    class Config:
        orm_mode = True

class UpdateAssetModel(BaseModel):
    asset_id: int
    name: Optional[str] = None
    description: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    latitude: Optional[str] = None
    longitude: Optional[str] = None
    status: Optional[int] = None
    
    class Config:
        orm_mode = True

class CreateAssetFileBase64Model(BaseModel):
    base64_str: str
    asset_id: int
    file_type: int
    
    class Config:
        orm_mode = True

class UpdateAssetFileBase64Model(BaseModel):
    file_id: int
    base64_str: Optional[str] = None
    status: Optional[int] = None
    
    class Config:
        orm_mode = True

class AssetTypeModel(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    file_url: Optional[str] = None
    slug: Optional[str] = None
    value_code: Optional[str] = None
    status: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    
    class Config:
        orm_mode = True

class AssetModel(BaseModel):
    id: int
    owner_id: int
    reference: str
    asset_type: int
    name: str
    description: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    latitude: Optional[str] = None
    longitude: Optional[str] = None
    status: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    
    class Config:
        orm_mode = True

class AssetFileModel(BaseModel):
    id: int
    asset_id: int
    file_type: int
    file_path: Optional[str] = None
    file_url: Optional[str] = None
    status: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    
    class Config:
        orm_mode = True
    
class AssetTypeResponseModel(BaseModel):
    status: bool
    message: str
    data: Optional[AssetTypeModel] = None

    class Config:
        orm_mode = True

class AssetResponseModel(BaseModel):
    status: bool
    message: str
    data: Optional[AssetModel] = None

    class Config:
        orm_mode = True

class AssetFileResponseModel(BaseModel):
    status: bool
    message: str
    data: Optional[AssetFileModel] = None

    class Config:
        orm_mode = True

class AssetWithFileModel(BaseModel):
    id: int
    owner_id: int
    reference: str
    asset_type: int
    name: str
    description: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    latitude: Optional[str] = None
    longitude: Optional[str] = None
    status: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    asset_files: Optional[List[AssetFileModel]] = None
    
    class Config:
        orm_mode = True

class AssetWithFilesResponseModel(BaseModel):
    status: bool
    message: str
    data: Optional[AssetWithFileModel] = None

    class Config:
        orm_mode = True
