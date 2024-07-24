from typing import Optional
from fastapi import APIRouter, Request, Depends, HTTPException, File, Form, UploadFile
from modules.authentication.auth import auth
from database.db import get_session
from sqlalchemy.orm import Session
from fastapi_pagination import LimitOffsetPage, Page
from database.schema import CreateRoomTypeModel, CreateRoomModel, UpdateRoomTypeModel, UpdateRoomModel, RoomTypeModel, RoomModel, RoomTypeResponseModel, RoomResponseModel, ResponseBasicModel, ErrorResponse
from modules.room_base.roo import insert_new_room_type, insert_new_room, update_existing_room_type, update_existing_room, retrieve_room_types, retrieve_rooms, retrieve_rooms_by_asset, retrieve_rooms_by_room_type, retrieve_rooms_by_asset_and_room_type, retrieve_rooms_by_control_box, retrieve_rooms_by_control_box_and_room_type, retrieve_single_room_type, retrieve_single_room, delete_existing_room_type, delete_existing_room

router = APIRouter(
    prefix="/v1/rooms",
    tags=["v1_rooms"]
)


@router.post("/types/create", response_model=RoomTypeResponseModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def create_room_type(request: Request, fields: CreateRoomTypeModel, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session)):
    req = insert_new_room_type(db=db, name=fields.name, description=fields.description, file_url=fields.file_url, value_code=fields.value_code, created_by=admin['id'])
    return req

@router.post("/create", response_model=RoomResponseModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def create_room(request: Request, fields: CreateRoomModel, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session)):
    req = insert_new_room(db=db, asset_id=fields.asset_id, room_type_id=fields.room_type_id, control_box_id=fields.control_box_id, name=fields.name, description=fields.description, created_by=admin['id'])
    return req

@router.post("/types/update/{room_type_id}", response_model=ResponseBasicModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def update_room_type(request: Request, fields: UpdateRoomTypeModel, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), room_type_id: int=0):
    updict = fields.model_dump()
    req = update_existing_room_type(db=db, room_type_id=room_type_id, values=updict, updated_by=admin['id'])
    return req

@router.post("/update/{room_id}", response_model=ResponseBasicModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def update_room(request: Request, fields: UpdateRoomModel, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), room_id: int=0):
    updict = fields.model_dump()
    req = update_existing_room(db=db, room_id=room_id, values=updict, updated_by=admin['id'])
    return req

@router.get("/types/get_all", response_model=Page[RoomTypeModel], responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_all_room_types(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session)):
    return retrieve_room_types(db=db)

@router.get("/get_all", response_model=Page[RoomModel], responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_all_rooms(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session)):
    return retrieve_rooms(db=db)

@router.get("/get_by_asset/{asset_id}", response_model=Page[RoomModel], responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_rooms_by_room(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), asset_id: int=0):
    return retrieve_rooms_by_asset(db=db, asset_id=asset_id)

@router.get("/get_by_room_type/{room_type_id}", response_model=Page[RoomModel], responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_rooms_by_room(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), room_type_id: int=0):
    return retrieve_rooms_by_room_type(db=db, room_type_id=room_type_id)

@router.get("/get_by_control_box/{control_box_id}", response_model=Page[RoomModel], responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_rooms_by_control_box(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), control_box_id: int=0):
    return retrieve_rooms_by_control_box(db=db, control_box_id=control_box_id)

@router.get("/get_by_asset_and_room_type/{asset_id}/{room_type_id}", response_model=Page[RoomModel], responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_ports_by_asset_and_room_type(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), asset_id: int=0, room_type_id: int=0):
    return retrieve_rooms_by_asset_and_room_type(db=db, asset_id=asset_id, room_type_id=room_type_id)

@router.get("/get_by_control_box_and_room_type/{control_box_id}/{room_type_id}", response_model=Page[RoomModel], responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_ports_by_control_box_and_room_type(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), control_box_id: int=0, room_type_id: int=0):
    return retrieve_rooms_by_control_box_and_room_type(db=db, control_box_id=control_box_id, room_type_id=room_type_id)

@router.get("/types/get_single/{room_type_id}", response_model=RoomTypeResponseModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_single_room_type(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), room_type_id: int = 0):
    return retrieve_single_room_type(db=db, room_type_id=room_type_id)

@router.get("/get_single/{room_id}", response_model=RoomResponseModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_single_room(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), room_id: int = 0):
    return retrieve_single_room(db=db, room_id=room_id)

@router.get("/types/delete/{room_type_id}", response_model=ResponseBasicModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def delete_room_type(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), room_type_id: int = 0):
    return delete_existing_room_type(db=db, room_type_id=room_type_id)

@router.get("/delete/{room_id}", response_model=ResponseBasicModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def delete_room(request: Request, admin=Depends(auth.auth_admin_wrapper), db: Session = Depends(get_session), room_id: int = 0):
    return delete_existing_room(db=db, room_id=room_id)
