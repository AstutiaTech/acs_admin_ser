from typing import Optional
from fastapi import APIRouter, Request, Depends, HTTPException, File, Form, UploadFile
from modules.authentication.auth import auth
from database.db import get_session
from sqlalchemy.orm import Session
from fastapi_pagination import LimitOffsetPage, Page
from database.schema import CreateControlBoxModel, UpdateControlBoxModel, ControlBoxModel, ControlBoxResponseModel, ResponseBasicModel, ErrorResponse
from modules.boxes.control import insert_control_box, update_existing_control_box, delete_existing_control_box, retrieve_all_control_boxes, retrieve_control_boxes_by_asset, retrieve_single_control_box

router = APIRouter(
    prefix="/v1/control_boxes",
    tags=["v1_control_boxes"]
)

@router.post("/create", response_model=ControlBoxResponseModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def create_control_box(request: Request, fields: CreateControlBoxModel, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session)):
    req = insert_control_box(db=db, asset_id=fields.asset_id, private_key=fields.private_key, comms_sim_card_value=fields.comms_sim_card_value, comms_sim_card_number=fields.comms_sim_card_number, comms_wifi_provider=fields.comms_wifi_provider, created_by=admin['id'])
    return req

@router.post("/update/{control_box_id}", response_model=ResponseBasicModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def update_control_box(request: Request, fields: UpdateControlBoxModel, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), control_box_id: int=0):
    updict = fields.model_dump()
    req = update_existing_control_box(db=db, control_box_id=control_box_id, values=updict, updated_by=admin['id'])
    return req

@router.get("/get_all", response_model=Page[ControlBoxModel], responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_all_control_boxes(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session)):
    return retrieve_all_control_boxes(db=db)

@router.get("/get_by_asset/{asset_id}", response_model=Page[ControlBoxModel], responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_by_control_box_by_asset(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), asset_id: int=0):
    return retrieve_control_boxes_by_asset(db=db, asset_id=asset_id)

@router.get("/get_single/{control_box_id}", response_model=ControlBoxResponseModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_single_control_box(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), control_box_id: int = 0):
    return retrieve_single_control_box(db=db, control_box_id=control_box_id)

@router.get("/delete/{control_box_id}", response_model=ResponseBasicModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def delete_control_box(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), control_box_id: int = 0):
    return delete_existing_control_box(db=db, control_box_id=control_box_id)
