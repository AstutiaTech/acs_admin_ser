from fastapi import APIRouter, Request, Depends, HTTPException
from modules.authentication.auth import auth
from database.db import get_session
from sqlalchemy.orm import Session
from fastapi_pagination import LimitOffsetPage, Page
from database.schema import CreateOwnerModel, UpdateOwnerModel, OwnerModel, OwnerResponseModel, ResponseBasicModel, ErrorResponse
from modules.users.base import insert_new_owner, update_existing_owner, retrieve_owners, retrieve_owners_by_status, retrieve_owners_search, retrieve_single_owner

router = APIRouter(
    prefix="/v1/owners",
    tags=["v1_owners"]
)

@router.post("/create", response_model=OwnerResponseModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def create_owner(request: Request, fields: CreateOwnerModel, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session)):
    req = insert_new_owner(db=db, name=fields.name, description=fields.description, created_by=admin['id'])
    return req

@router.post("/update/{owner_id}", response_model=ResponseBasicModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def update_owner(request: Request, fields: UpdateOwnerModel, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), owner_id: int=0):
    updict = fields.model_dump()
    req = update_existing_owner(db=db, owner_id=owner_id, values=updict, updated_by=admin['id'])
    return req

@router.get("/get_all", response_model=Page[OwnerModel], responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_all_owners(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session)):
    return retrieve_owners(db=db)

@router.get("/get_by_status/{status}", response_model=Page[OwnerModel], responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_owner_by_status(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), status: int = 0):
    return retrieve_owners_by_status(db=db, status=status)

@router.get("/search/{query}", response_model=Page[OwnerModel], responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def search_owners(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), query: str = ''):
    return retrieve_owners_search(db=db, query=query)

@router.get("/get_single/{owner_id}", response_model=OwnerResponseModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_single_owner(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), owner_id: int = 0):
    return retrieve_single_owner(db=db, owner_id=owner_id)
