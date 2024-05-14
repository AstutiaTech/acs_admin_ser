from typing import Optional
from fastapi import APIRouter, Request, Depends, HTTPException, File, Form, UploadFile
from modules.authentication.auth import auth
from database.db import get_session
from sqlalchemy.orm import Session
from fastapi_pagination import LimitOffsetPage, Page
from database.schema import CreateAssetModel, UpdateAssetModel, CreateAssetFileBase64Model, UpdateAssetFileBase64Model, AssetModel, AssetFileModel, AssetResponseModel, AssetFileResponseModel, AssetWithFileModel, AssetWithFilesResponseModel, ResponseBasicModel, ErrorResponse
from modules.assets.asset_main import insert_new_asset, update_existing_asset, insert_new_asset_file_form_data, insert_new_asset_file_base64, update_existing_asset_file_form_data, update_existing_asset_file_base64, delete_existing_asset, delete_existing_asset_file, retrieve_assets, retrieve_assets_with_files, retrieve_assets_by_owners, retrieve_assets_by_owners_with_files, retrieve_single_asset, retrieve_single_asset_with_files, retrieve_all_asset_files, retrieve_all_asset_files_by_asset, retrieve_single_asset_file

router = APIRouter(
    prefix="/v1/assets",
    tags=["v1_assets"]
)


@router.post("/create", response_model=AssetResponseModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def create(request: Request, fields: CreateAssetModel, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session)):
    req = insert_new_asset(db=db, owner_id=fields.owner_id, asset_type=fields.asset_type, name=fields.name, description=fields.description, address=fields.address, city=fields.city, state=fields.state, country=fields.country, latitude=fields.latitude, longitude=fields.longitude)
    return req

@router.post("/update/{asset_id}", response_model=ResponseBasicModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def update(request: Request, fields: UpdateAssetModel, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), asset_id: int=0):
    updict = fields.model_dump()
    req = update_existing_asset(db=db, asset_id=asset_id, values=updict)
    return req

@router.post("/files/create_form", response_model=AssetFileResponseModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def files_create_form(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session=Depends(get_session), uploaded_file: UploadFile = File(), asset_id: int=Form(), file_type: int=Form()):
    req = insert_new_asset_file_form_data(db=db, uploaded_file=uploaded_file, asset_id=asset_id, file_type=file_type)
    return req

@router.post("/files/create_base64", response_model=AssetFileResponseModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def files_create_base64(request: Request, fields: CreateAssetFileBase64Model, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session)):
    req = insert_new_asset_file_base64(db=db, base64_str=fields.base64_str, asset_id=fields.asset_id, file_type=fields.file_type)
    return req

@router.post("/files/update_form", response_model=ResponseBasicModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def files_update_form(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session=Depends(get_session), uploaded_file: Optional[UploadFile] = File(None), file_id: int=Form(), status: Optional[int]=Form(None)):
    req = update_existing_asset_file_form_data(db=db, file_id=file_id, uploaded_file=uploaded_file, status=status)
    return req

@router.post("/files/update_base64", response_model=ResponseBasicModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def files_update_base64(request: Request, fields: UpdateAssetFileBase64Model, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session)):
    req = update_existing_asset_file_base64(db=db, file_id=fields.file_id, base64_str=fields.base64_str, status=fields.status)
    return req

@router.get("/get_all", response_model=Page[AssetModel], responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_all(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session)):
    return retrieve_assets(db=db)

@router.get("/get_all_with_files", response_model=Page[AssetWithFileModel], responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_all_with_files(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session)):
    return retrieve_assets_with_files(db=db)

@router.get("/get_by_owner/{owner_id}", response_model=Page[AssetModel], responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_by_owner(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), owner_id: int=0):
    return retrieve_assets_by_owners(db=db, owner_id=owner_id)

@router.get("/get_by_owner_with_files/{owner_id}", response_model=Page[AssetWithFileModel], responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_all_with_files(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), owner_id: int=0):
    return retrieve_assets_by_owners_with_files(db=db, owner_id=owner_id)

@router.get("/get_single/{asset_id}", response_model=AssetResponseModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_single(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), asset_id: int = 0):
    return retrieve_single_asset(db=db, asset_id=asset_id)

@router.get("/get_single_with_file/{asset_id}", response_model=AssetWithFilesResponseModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_single_with_file(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), asset_id: int = 0):
    return retrieve_single_asset_with_files(db=db, asset_id=asset_id)

@router.get("/files/get_all", response_model=Page[AssetFileModel], responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def files_get_all(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session)):
    return retrieve_all_asset_files(db=db)

@router.get("/files/get_by_asset/{asset_id}", response_model=Page[AssetFileModel], responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def files_get_all(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), asset_id: int=0):
    return retrieve_all_asset_files_by_asset(db=db, asset_id=asset_id)

@router.get("/files/get_single/{file_id}", response_model=AssetResponseModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def files_get_single(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), file_id: int = 0):
    return retrieve_single_asset_file(db=db, file_id=file_id)

@router.get("/delete/{asset_id}", response_model=ResponseBasicModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def delete(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), asset_id: int = 0):
    return delete_existing_asset(db=db, asset_id=asset_id)

@router.get("/files/delete/{file_id}", response_model=ResponseBasicModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def files_delete(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), file_id: int = 0):
    return delete_existing_asset_file(db=db, file_id=file_id)
