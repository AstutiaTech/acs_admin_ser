from typing import Optional
from fastapi import APIRouter, Request, Depends, HTTPException, File, Form, UploadFile
from modules.authentication.auth import auth
from database.db import get_session
from sqlalchemy.orm import Session
from fastapi_pagination import LimitOffsetPage, Page
from database.schema import CreateInverterModel, UpdateInverterModel, InverterModel, InverterResponseModel, ResponseBasicModel, ErrorResponse
from modules.inverters.inv import insert_new_inverter, update_existing_inverter, retrieve_inverters, retrieve_inverters_by_control_box, retrieve_single_inverter, delete_existing_inverter

router = APIRouter(
    prefix="/v1/inverters",
    tags=["v1_inverters"]
)


@router.post("/create", response_model=InverterResponseModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def create_inverter(request: Request, fields: CreateInverterModel, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session)):
    req = insert_new_inverter(db=db, control_box_id=fields.control_box_id, capacity=fields.capacity, voltage_input=fields.voltage_input, voltage_output=fields.voltage_output)
    return req

@router.post("/update/{inverter_id}", response_model=ResponseBasicModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def update_inverter(request: Request, fields: UpdateInverterModel, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), inverter_id: int=0):
    updict = fields.model_dump()
    req = update_existing_inverter(db=db, inverter_id=inverter_id, values=updict)
    return req

@router.get("/get_all", response_model=Page[InverterModel], responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_all_inverters(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session)):
    return retrieve_inverters(db=db)

@router.get("/get_by_control_box/{control_box_id}", response_model=Page[InverterModel], responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_inverters_by_control_box(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), control_box_id: int=0):
    return retrieve_inverters_by_control_box(db=db, control_box_id=control_box_id)

@router.get("/get_single/{inverter_id}", response_model=InverterResponseModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_single_inverter(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), inverter_id: int = 0):
    return retrieve_single_inverter(db=db, inverter_id=inverter_id)

@router.get("/delete/{inverter_id}", response_model=ResponseBasicModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def delete_inverter(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), inverter_id: int = 0):
    return delete_existing_inverter(db=db, inverter_id=inverter_id)
