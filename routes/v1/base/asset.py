from typing import Optional
from fastapi import APIRouter, Request, Depends, HTTPException, File, Form, UploadFile
from modules.authentication.auth import auth
from database.db import get_session
from sqlalchemy.orm import Session
from fastapi_pagination import LimitOffsetPage, Page
from database.schema import CreateAssetTypeModel, CreateAssetModel, UpdateAssetTypeModel, UpdateAssetModel, CreateAssetFileBase64Model, UpdateAssetFileBase64Model, AssetTypeModel, AssetModel, AssetFileModel, AssetTypeResponseModel, AssetResponseModel, AssetFileResponseModel, AssetWithFileModel, AssetWithFilesResponseModel, ResponseBasicModel, ErrorResponse
from modules.assets.asset_main import insert_new_asset_type, insert_new_asset, update_existing_asset_type, update_existing_asset, insert_new_asset_file_form_data, insert_new_asset_file_base64, update_existing_asset_file_form_data, update_existing_asset_file_base64, delete_existing_asset_type, delete_existing_asset, delete_existing_asset_file, retrive_asset_type, retrieve_assets, retrieve_assets_with_files, retrieve_assets_by_owners, retrieve_assets_by_owners_with_files, retrieve_assets_by_asset_type, retrieve_assets_by_asset_type_with_files, retrive_single_asset_type, retrieve_assets_by_owner_and_asset_type, retrieve_assets_by_owner_and_asset_type_with_files, retrieve_single_asset, retrieve_single_asset_with_files, retrieve_all_asset_files, retrieve_all_asset_files_by_asset, retrieve_single_asset_file

router = APIRouter(
    prefix="/v1/assets",
    tags=["v1_assets"]
)

@router.post("/types/create", response_model=AssetTypeResponseModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def create_asset_type(request: Request, fields: CreateAssetTypeModel, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session)):
    req = insert_new_asset_type(db=db, name=fields.name, description=fields.description, file_url=fields.file_url, value_code=fields.value_code, created_by=admin['id'])
    return req

@router.post("/create", response_model=AssetResponseModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def create_asset(request: Request, fields: CreateAssetModel, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session)):
    req = insert_new_asset(db=db, owner_id=fields.owner_id, asset_type_id=fields.asset_type_id, name=fields.name, description=fields.description, address=fields.address, city=fields.city, state=fields.state, country=fields.country, latitude=fields.latitude, longitude=fields.longitude, created_by=admin['id'])
    return req

@router.post("/types/update/{asset_type_id}", response_model=ResponseBasicModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def update_asset_type(request: Request, fields: UpdateAssetTypeModel, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), asset_type_id: int=0):
    updict = fields.model_dump()
    req = update_existing_asset_type(db=db, asset_type_id=asset_type_id, values=updict, updated_by=admin['id'])
    return req

@router.post("/update/{asset_id}", response_model=ResponseBasicModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def update_asset(request: Request, fields: UpdateAssetModel, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), asset_id: int=0):
    updict = fields.model_dump()
    req = update_existing_asset(db=db, asset_id=asset_id, values=updict, updated_by=admin['id'])
    return req

@router.post("/files/create_form", response_model=AssetFileResponseModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def create_asset_files_create_by_form_data(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session=Depends(get_session), uploaded_file: UploadFile = File(), asset_id: int=Form(), file_type: int=Form()):
    req = insert_new_asset_file_form_data(db=db, uploaded_file=uploaded_file, asset_id=asset_id, file_type=file_type, created_by=admin['id'])
    return req

@router.post("/files/create_base64", response_model=AssetFileResponseModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def create_asset_files_create_by_base64(request: Request, fields: CreateAssetFileBase64Model, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session)):
    req = insert_new_asset_file_base64(db=db, base64_str=fields.base64_str, asset_id=fields.asset_id, file_type=fields.file_type, created_by=admin['id'])
    return req

@router.post("/files/update_form", response_model=ResponseBasicModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def asset_file_update_by_form_data(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session=Depends(get_session), uploaded_file: Optional[UploadFile] = File(None), file_id: int=Form(), status: Optional[int]=Form(None)):
    req = update_existing_asset_file_form_data(db=db, file_id=file_id, uploaded_file=uploaded_file, status=status, updated_by=admin['id'])
    return req

@router.post("/files/update_base64", response_model=ResponseBasicModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def asset_file_update_by_base64(request: Request, fields: UpdateAssetFileBase64Model, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session)):
    req = update_existing_asset_file_base64(db=db, file_id=fields.file_id, base64_str=fields.base64_str, status=fields.status, updated_by=admin['id'])
    return req

@router.get("/types/get_all", response_model=Page[AssetTypeModel], responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_all_asset_types(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session)):
    return retrive_asset_type(db=db)

@router.get("/get_all", response_model=Page[AssetModel], responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_all_assets(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session)):
    return retrieve_assets(db=db)

@router.get("/get_all_with_files", response_model=Page[AssetWithFileModel], responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_all_assets_with_files(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session)):
    return retrieve_assets_with_files(db=db)

@router.get("/get_by_owner/{owner_id}", response_model=Page[AssetModel], responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_assets_by_owner(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), owner_id: int=0):
    return retrieve_assets_by_owners(db=db, owner_id=owner_id)

@router.get("/get_by_owner_with_files/{owner_id}", response_model=Page[AssetWithFileModel], responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_assets_by_owner_all_with_files(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), owner_id: int=0):
    return retrieve_assets_by_owners_with_files(db=db, owner_id=owner_id)

@router.get("/get_by_asset_type/{asset_type_id}", response_model=Page[AssetModel], responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_assets_by_asset_type(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), asset_type_id: int=0):
    return retrieve_assets_by_asset_type(db=db, asset_type_id=asset_type_id)

@router.get("/get_by_asset_type_with_files/{asset_type_id}", response_model=Page[AssetWithFileModel], responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_assets_by_asset_type_all_with_files(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), asset_type_id: int=0):
    return retrieve_assets_by_asset_type_with_files(db=db, asset_type_id=asset_type_id)

@router.get("/get_by_owner_and_asset_type/{owner_id}/{asset_type_id}", response_model=Page[AssetModel], responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_assets_by_owner_and_asset_type(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), owner_id: int=0, asset_type_id: int=0):
    return retrieve_assets_by_owner_and_asset_type(db=db, owner_id=owner_id, asset_type_id=asset_type_id)

@router.get("/get_by_owner_and_asset_type_with_files/{owner_id}/{asset_type_id}", response_model=Page[AssetWithFileModel], responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_assets_by_owner_and_asset_type_all_with_files(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), owner_id: int=0, asset_type_id: int=0):
    return retrieve_assets_by_owner_and_asset_type_with_files(db=db, owner_id=owner_id, asset_type_id=asset_type_id)

@router.get("/types/get_single/{asset_type_id}", response_model=AssetTypeResponseModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_single_asset_type(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), asset_type_id: int = 0):
    return retrive_single_asset_type(db=db, asset_type_id=asset_type_id)

@router.get("/get_single/{asset_id}", response_model=AssetResponseModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_single_asset(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), asset_id: int = 0):
    return retrieve_single_asset(db=db, asset_id=asset_id)

@router.get("/get_single_with_file/{asset_id}", response_model=AssetWithFilesResponseModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_single_asset_with_file(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), asset_id: int = 0):
    return retrieve_single_asset_with_files(db=db, asset_id=asset_id)

@router.get("/files/get_all", response_model=Page[AssetFileModel], responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def asset_files_get_all(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session)):
    return retrieve_all_asset_files(db=db)

@router.get("/files/get_by_asset/{asset_id}", response_model=Page[AssetFileModel], responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def asset_files_get_all_by_asset(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), asset_id: int=0):
    return retrieve_all_asset_files_by_asset(db=db, asset_id=asset_id)

@router.get("/files/get_single/{file_id}", response_model=AssetResponseModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def asset_files_get_single(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), file_id: int = 0):
    return retrieve_single_asset_file(db=db, file_id=file_id)

@router.get("/types/delete/{asset_type_id}", response_model=ResponseBasicModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def delete_asset_type(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), asset_type_id: int = 0):
    return delete_existing_asset_type(db=db, asset_type_id=asset_type_id)

@router.get("/delete/{asset_id}", response_model=ResponseBasicModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def delete_asset(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), asset_id: int = 0):
    return delete_existing_asset(db=db, asset_id=asset_id)

@router.get("/files/delete/{file_id}", response_model=ResponseBasicModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def files_delete_asset_file(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), file_id: int = 0):
    return delete_existing_asset_file(db=db, file_id=file_id)
