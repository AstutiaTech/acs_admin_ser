from fastapi import APIRouter, Request, Depends, HTTPException
from modules.authentication.auth import auth
from database.db import get_session
from sqlalchemy.orm import Session
from fastapi_pagination import LimitOffsetPage, Page
from database.schema import CreateUserModel, UpdateUserModel, UserModel, UserResponseModel, ResponseBasicModel, ErrorResponse
from modules.users.base import create_new_user, update_existing_user, retrieve_users, retrieve_users_by_owners, retrieve_users_by_owners_and_status, retrieve_users_search, retrieve_single_user

router = APIRouter(
    prefix="/v1/users",
    tags=["v1_users"]
)

@router.post("/create", response_model=UserResponseModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def create(request: Request, fields: CreateUserModel, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session)):
    req = create_new_user(db=db, owner_id=fields.owner_id, username=fields.username, email=fields.email, password=fields.password, role=fields.role)
    return req

@router.post("/update/{user_id}", response_model=ResponseBasicModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def create(request: Request, fields: UpdateUserModel, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), user_id: int=0):
    updict = fields.model_dump()
    req = update_existing_user(db=db, user_id=user_id, values=updict)
    return req

@router.get("/get_all", response_model=Page[UserModel], responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_all(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session)):
    return retrieve_users(db=db)

@router.get("/get_by_owners/{owner_id}", response_model=Page[UserModel], responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_by_owners(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), owner_id: int = 0):
    return retrieve_users_by_owners(db=db, owner_id=owner_id)

@router.get("/get_by_owners_and_status/{owner_id}/{status}", response_model=Page[UserModel], responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_by_owners_and_status(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), owner_id: int = 0, status: int = 0):
    return retrieve_users_by_owners_and_status(db=db, owner_id=owner_id, status=status)

@router.get("/search/{query}", response_model=Page[UserModel], responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def search(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), query: str = ''):
    return retrieve_users_search(db=db, query=query)

@router.get("/get_single/{user_id}", response_model=UserResponseModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_single(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), user_id: int = 0):
    return retrieve_single_user(db=db, user_id=user_id)
