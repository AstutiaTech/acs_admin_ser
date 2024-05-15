from typing import Optional
from fastapi import APIRouter, Request, Depends, HTTPException, File, Form, UploadFile
from modules.authentication.auth import auth
from database.db import get_session
from sqlalchemy.orm import Session
from fastapi_pagination import LimitOffsetPage, Page
from database.schema import CreatePortModel, UpdatePortModel, PortModel, PortResponseModel, ResponseBasicModel, ErrorResponse
from modules.port_base.por import insert_new_port, update_existing_port, delete_existing_port, retrieve_ports, retrieve_ports_by_control_box, retrieve_single_port

router = APIRouter(
    prefix="/v1/ports",
    tags=["v1_ports"]
)


@router.post("/create", response_model=PortResponseModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def create(request: Request, fields: CreatePortModel, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session)):
    req = insert_new_port(db=db, control_box_id=fields.control_box_id, appliance_name=fields.appliance_name, room_name=fields.room_name, power_rating=fields.power_rating, current_drawn=fields.current_drawn, priority_status=fields.priority_status)
    return req

@router.post("/update/{port_id}", response_model=ResponseBasicModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def update(request: Request, fields: UpdatePortModel, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), port_id: int=0):
    updict = fields.model_dump()
    req = update_existing_port(db=db, port_id=port_id, values=updict)
    return req

@router.get("/get_all", response_model=Page[PortModel], responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_all(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session)):
    return retrieve_ports(db=db)

@router.get("/get_by_control_box/{control_box_id}", response_model=Page[PortModel], responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_by_control_box(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), control_box_id: int=0):
    return retrieve_ports_by_control_box(db=db, control_box_id=control_box_id)

@router.get("/get_single/{port_id}", response_model=PortResponseModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_single(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), port_id: int = 0):
    return retrieve_single_port(db=db, port_id=port_id)

@router.get("/delete/{port_id}", response_model=ResponseBasicModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def delete(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), port_id: int = 0):
    return delete_existing_port(db=db, port_id=port_id)
