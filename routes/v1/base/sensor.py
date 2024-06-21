from typing import Optional
from fastapi import APIRouter, Request, Depends, HTTPException, File, Form, UploadFile
from modules.authentication.auth import auth
from database.db import get_session
from sqlalchemy.orm import Session
from fastapi_pagination import LimitOffsetPage, Page
from database.schema import CreateSensorModel, UpdateSensorModel, SensorModel, SensorResponseModel, ResponseBasicModel, ErrorResponse
from modules.sensor_base.sens import insert_new_sensor, update_existing_sensor, delete_existing_sensor, retrieve_sensors, retrieve_sensors_by_control_box, retrieve_single_sensor

router = APIRouter(
    prefix="/v1/sensors",
    tags=["v1_sensors"]
)


@router.post("/create", response_model=SensorResponseModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def create_sensor(request: Request, fields: CreateSensorModel, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session)):
    req = insert_new_sensor(db=db, control_box_id=fields.control_box_id, sensor_type=fields.sensor_type, voltage_input=fields.voltage_input, voltage_output=fields.voltage_output)
    return req

@router.post("/update/{sensor_id}", response_model=ResponseBasicModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def update_sensor(request: Request, fields: UpdateSensorModel, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), sensor_id: int=0):
    updict = fields.model_dump()
    req = update_existing_sensor(db=db, sensor_id=sensor_id, values=updict)
    return req

@router.get("/get_all", response_model=Page[SensorModel], responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_all_sensors(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session)):
    return retrieve_sensors(db=db)

@router.get("/get_by_control_box/{control_box_id}", response_model=Page[SensorModel], responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_sensors_by_control_box(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), control_box_id: int=0):
    return retrieve_sensors_by_control_box(db=db, control_box_id=control_box_id)

@router.get("/get_single/{sensor_id}", response_model=SensorResponseModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_single_sensor(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), sensor_id: int = 0):
    return retrieve_single_sensor(db=db, sensor_id=sensor_id)

@router.get("/delete/{sensor_id}", response_model=ResponseBasicModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def delete_sensor(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), sensor_id: int = 0):
    return delete_existing_sensor(db=db, sensor_id=sensor_id)
