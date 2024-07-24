from typing import Optional
from fastapi import APIRouter, Request, Depends, HTTPException, File, Form, UploadFile
from modules.authentication.auth import auth
from database.db import get_session
from sqlalchemy.orm import Session
from fastapi_pagination import LimitOffsetPage, Page
from database.schema import CreatePortTypeModel, CreatePortModel, UpdatePortTypeModel, UpdatePortModel, PortTypeModel, PortModel, PortTypeResponseModel, PortResponseModel, ResponseBasicModel, ErrorResponse
from modules.port_base.por import insert_new_port_type, insert_new_port, update_existing_port_type, update_existing_port, delete_existing_port_type, delete_existing_port, retrieve_port_types, retrieve_ports, retrieve_ports_by_room, retrieve_ports_by_control_box, retrieve_ports_by_port_type, retrieve_ports_by_control_box_and_port_type, retrieve_ports_by_room_and_port_type, retrieve_single_port_type, retrieve_single_port

router = APIRouter(
    prefix="/v1/ports",
    tags=["v1_ports"]
)


@router.post("/types/create", response_model=PortTypeResponseModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def create_port_type(request: Request, fields: CreatePortTypeModel, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session)):
    req = insert_new_port_type(db=db, name=fields.name, description=fields.description, file_url=fields.file_url, value_code=fields.value_code, created_by=admin['id'])
    return req

@router.post("/create", response_model=PortResponseModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def create_port(request: Request, fields: CreatePortModel, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session)):
    req = insert_new_port(db=db, control_box_id=fields.control_box_id, appliance_name=fields.appliance_name, room_name=fields.room_name, power_rating=fields.power_rating, current_drawn=fields.current_drawn, priority_status=fields.priority_status, created_by=admin['id'])
    return req

@router.post("/types/update/{port_type_id}", response_model=ResponseBasicModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def update_port_type(request: Request, fields: UpdatePortTypeModel, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), port_type_id: int=0):
    updict = fields.model_dump()
    req = update_existing_port_type(db=db, port_type_id=port_type_id, values=updict, updated_by=admin['id'])
    return req

@router.post("/update/{port_id}", response_model=ResponseBasicModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def update_port(request: Request, fields: UpdatePortModel, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), port_id: int=0):
    updict = fields.model_dump()
    req = update_existing_port(db=db, port_id=port_id, values=updict, updated_by=admin['id'])
    return req

@router.get("/types/get_all", response_model=Page[PortTypeModel], responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_all_port_types(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session)):
    return retrieve_port_types(db=db)

@router.get("/get_all", response_model=Page[PortModel], responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_all_ports(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session)):
    return retrieve_ports(db=db)

@router.get("/get_by_room/{room_id}", response_model=Page[PortModel], responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_ports_by_room(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), room_id: int=0):
    return retrieve_ports_by_room(db=db, room_id=room_id)

@router.get("/get_by_control_box/{control_box_id}", response_model=Page[PortModel], responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_ports_by_control_box(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), control_box_id: int=0):
    return retrieve_ports_by_control_box(db=db, control_box_id=control_box_id)

@router.get("/get_by_port_type/{port_type_id}", response_model=Page[PortModel], responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_ports_by_port_type(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), port_type_id: int=0):
    return retrieve_ports_by_port_type(db=db, port_type_id=port_type_id)

@router.get("/get_by_control_box_and_port_type/{control_box_id}/{port_type_id}", response_model=Page[PortModel], responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_ports_by_control_box_and_port_type(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), control_box_id: int=0, port_type_id: int=0):
    return retrieve_ports_by_control_box_and_port_type(db=db, control_box_id=control_box_id, port_type_id=port_type_id)

@router.get("/get_by_room_and_port_type/{room_id}/{port_type_id}", response_model=Page[PortModel], responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_ports_by_room_and_port_type(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), room_id: int=0, port_type_id: int=0):
    return retrieve_ports_by_room_and_port_type(db=db, room_id=room_id, port_type_id=port_type_id)

@router.get("/types/get_single/{port_type_id}", response_model=PortTypeResponseModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_single_port_type(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), port_type_id: int = 0):
    return retrieve_single_port_type(db=db, port_type_id=port_type_id)

@router.get("/get_single/{port_id}", response_model=PortResponseModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_single_port(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), port_id: int = 0):
    return retrieve_single_port(db=db, port_id=port_id)

@router.get("/types/delete/{port_type_id}", response_model=ResponseBasicModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def delete_port_type(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), port_type_id: int = 0):
    return delete_existing_port_type(db=db, port_type_id=port_type_id)

@router.get("/delete/{port_id}", response_model=ResponseBasicModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def delete_port(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), port_id: int = 0):
    return delete_existing_port(db=db, port_id=port_id)
