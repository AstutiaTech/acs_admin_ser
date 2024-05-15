from typing import Optional
from fastapi import APIRouter, Request, Depends, HTTPException, File, Form, UploadFile
from modules.authentication.auth import auth
from database.db import get_session
from sqlalchemy.orm import Session
from fastapi_pagination import LimitOffsetPage, Page
from database.schema import CreateBatteryModel, UpdateBatteryModel, BatteryModel, BatteryResponseModel, ResponseBasicModel, ErrorResponse
from modules.batteries.bat import insert_new_battery, update_existing_battery, delete_existing_battery, retrieve_batteries, retrieve_batteries_by_control_box, retrieve_single_battery

router = APIRouter(
    prefix="/v1/batteries",
    tags=["v1_batteries"]
)

@router.post("/create", response_model=BatteryResponseModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def create(request: Request, fields: CreateBatteryModel, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session)):
    req = insert_new_battery(db=db, control_box_id=fields.control_box_id, state_of_charge=fields.state_of_charge, current_drawn=fields.current_drawn, voltage=fields.voltage, capacity=fields.capacity)
    return req

@router.post("/update/{battery_id}", response_model=ResponseBasicModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def update(request: Request, fields: UpdateBatteryModel, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), battery_id: int=0):
    updict = fields.model_dump()
    req = update_existing_battery(db=db, battery_id=battery_id, values=updict)
    return req

@router.get("/get_all", response_model=Page[BatteryModel], responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_all(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session)):
    return retrieve_batteries(db=db)

@router.get("/get_by_control_box/{control_box_id}", response_model=Page[BatteryModel], responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_by_control_box(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), control_box_id: int=0):
    return retrieve_batteries_by_control_box(db=db, control_box_id=control_box_id)

@router.get("/get_single/{battery_id}", response_model=BatteryResponseModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_single(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), battery_id: int = 0):
    return retrieve_single_battery(db=db, battery_id=battery_id)

@router.get("/delete/{battery_id}", response_model=ResponseBasicModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def delete(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), battery_id: int = 0):
    return delete_existing_battery(db=db, battery_id=battery_id)
