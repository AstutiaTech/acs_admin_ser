from typing import Dict
from database.model import create_room_type, create_room, update_room_type, update_room, delete_room_type, delete_room, get_all_room_types, get_all_rooms, get_all_rooms_by_asset_id, get_all_rooms_by_room_type_id, get_all_rooms_by_asset_id_and_room_type_id, get_all_rooms_by_control_box_id, get_all_rooms_by_control_box_id_and_room_type_id, get_room_type_by_id, get_room_by_id
from sqlalchemy.orm import Session
from fastapi_pagination.ext.sqlalchemy import paginate
from modules.utils.tools import process_schema_dictionary, slugify

def insert_new_room_type(db: Session, asset_type_id: int=0, name: str=None, description: str=None, file_url: str=None, value_code: str=None, created_by: int=0):
    slug = slugify(input_string=name, strip='_')
    room_type = create_room_type(db=db, asset_type_id=asset_type_id, name=name, description=description, file_url=file_url, slug=slug, value_code=value_code, status=1, created_by=created_by)
    return {
        'status': True,
        'message': 'Success',
        'data': room_type,
    }

def insert_new_room(db: Session, asset_id: int=0, room_type_id: int=0, control_box_id: int=0, name: str=None, description: str=None, created_by: int=0):
    room = create_room(db=db, asset_id=asset_id, room_type_id=room_type_id, control_box_id=control_box_id, name=name, description=description, created_by=created_by)
    return {
        'status': True,
        'message': 'Success',
        'data': room,
    }

def update_existing_room_type(db: Session, room_type_id: int=0, values: Dict={}, updated_by: int=0):
    values = process_schema_dictionary(info=values)
    values['updated_by'] = updated_by
    update_room_type(db=db, id=room_type_id, values=values)
    return {
        'status': True,
        'message': 'Success',
    }

def update_existing_room(db: Session, room_id: int=0, values: Dict={}, updated_by: int=0):
    values = process_schema_dictionary(info=values)
    values['updated_by'] = updated_by
    update_room(db=db, id=room_id, values=values)
    return {
        'status': True,
        'message': 'Success',
    }

def delete_existing_room_type(db: Session, room_type_id: int=0):
    delete_room_type(db=db, id=room_type_id)
    return {
        'status': True,
        'message': 'Success',
    }

def delete_existing_room(db: Session, room_id: int=0):
    delete_room(db=db, id=room_id)
    return {
        'status': True,
        'message': 'Success',
    }

def retrieve_room_types(db: Session):
    data = get_all_room_types(db=db)
    return paginate(data)

def retrieve_rooms(db: Session):
    data = get_all_rooms(db=db)
    return paginate(data)

def retrieve_rooms_by_asset(db: Session, asset_id: int=0):
    data = get_all_rooms_by_asset_id(db=db, asset_id=asset_id)
    return paginate(data)

def retrieve_rooms_by_room_type(db: Session, room_type_id: int=0):
    data = get_all_rooms_by_room_type_id(db=db, room_type_id=room_type_id)
    return paginate(data)

def retrieve_rooms_by_asset_and_room_type(db: Session, asset_id: int=0, room_type_id: int=0):
    data = get_all_rooms_by_asset_id_and_room_type_id(db=db, asset_id=asset_id, room_type_id=room_type_id)
    return paginate(data)

def retrieve_rooms_by_control_box(db: Session, control_box_id: int=0):
    data = get_all_rooms_by_control_box_id(db=db, control_box_id=control_box_id)
    return paginate(data)

def retrieve_rooms_by_control_box_and_room_type(db: Session, control_box_id: int=0, room_type_id: int=0):
    data = get_all_rooms_by_control_box_id_and_room_type_id(db=db, control_box_id=control_box_id, room_type_id=room_type_id)
    return paginate(data)

def retrieve_single_room_type(db: Session, room_type_id: int=0):
    room_type = get_room_type_by_id(db=db, id=room_type_id)
    if room_type is None:
        return {
            'status': False,
            'message': 'Not found',
            'data': None,
        }
    else:
        return {
            'status': True,
            'message': 'Success',
            'data': room_type,
        }
    
def retrieve_single_room(db: Session, room_id: int=0):
    room = get_room_by_id(db=db, id=room_id)
    if room is None:
        return {
            'status': False,
            'message': 'Not found',
            'data': None,
        }
    else:
        return {
            'status': True,
            'message': 'Success',
            'data': room,
        }
