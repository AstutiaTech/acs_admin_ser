from fastapi import APIRouter, Request, Depends, HTTPException
from typing import List
from modules.authentication.auth import auth
from database.schema import LoginModel, RegisterModel, AuthResponseModel, UpdateAdminModel, UpdateAdminPasswordModel, ResponseBasicModel, ErrorResponse
from modules.authentication.auth import login_admin, register_admin, get_loggedin_admin, update_admin_details, update_admin_password
from database.db import get_session, get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/v1/auth",
    tags=["v1_auth"]
)

@router.post("/register", response_model=AuthResponseModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def register(fields: RegisterModel, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session)):
    """
    Register new admin
    """
    req = register_admin(db=db, role=fields.role, username=fields.username, email=fields, password=fields.password, created_by=admin['id'])
    return req

@router.post("/login")
async def login(fields: LoginModel, db: Session = Depends(get_db)):
    """
    Login
    """
    req = login_admin(db=db, field=fields.field, password=fields.password)
    return req

@router.get("/details", response_model=List[AuthResponseModel], responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def details(admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session)):
    """
    Loggedin user details
    """
    return get_loggedin_admin(db=db, admin_id=admin['id'])

@router.post("/update", response_model=ResponseBasicModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def update(fields: UpdateAdminModel, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session)):
    """
    Update admin details
    """
    req = update_admin_details(db=db, admin_id=admin['id'], values=dict(fields), updated_by=admin['id'])
    return req
    
@router.post("/update_password", response_model=ResponseBasicModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def update_password(fields: UpdateAdminPasswordModel, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session)):
    """
    Update admin password
    """
    req = update_admin_password(db=db, admin_id=admin['id'], password=fields.password, password_confirmation=fields.password_confirmation, old_password=fields.old_password)
    return req
    