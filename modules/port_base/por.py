from typing import Dict
from database.model import create_port_type, create_port, update_port_type, update_port, delete_port_type, delete_port, get_all_port_types, get_port_type_by_id, get_all_ports, get_all_ports_by_room_id, get_all_ports_by_control_box_id, get_all_ports_by_room_id_and_port_type_id, get_all_ports_by_control_box_id_and_port_type_id, get_all_ports_by_port_type_id, get_port_by_id
from sqlalchemy.orm import Session
from fastapi_pagination.ext.sqlalchemy import paginate
from modules.utils.tools import process_schema_dictionary, generate_basic_reference, slugify

def insert_new_port_type(db: Session, name: str=None, description: str=None, file_url: str=None, value_code: str=None, created_by: int=0):
    slug = slugify(input_string=name, strip='_')
    port_type = create_port_type(db=db, name=name, description=description, file_url=file_url, slug=slug, value_code=value_code, status=1, created_by=created_by)
    return {
        'status': True,
        'message': 'Success',
        'data': port_type,
    }

def insert_new_port(db: Session, room_id: int=0, control_box_id: int=0, port_type_id: int=0, appliance_name: str=None, room_name: str=None, power_rating: str=None, current_drawn: str=None, priority_status: int=0, created_by: int=0):
    reference = generate_basic_reference()
    port = create_port(db=db, room_id=room_id, control_box_id=control_box_id, port_type_id=port_type_id, reference=reference, appliance_name=appliance_name, room_name=room_name, power_rating=power_rating, current_drawn=current_drawn, priority_status=priority_status, status=1, created_by=created_by)
    return {
        'status': True,
        'message': 'Success',
        'data': port,
    }

def update_existing_port_type(db: Session, port_type_id: int=0, values: Dict={}, updated_by: int=0):
    values = process_schema_dictionary(info=values)
    values['updated_by'] = updated_by
    update_port_type(db=db, id=port_type_id, values=values)
    return {
        'status': True,
        'message': 'Success',
    }

def update_existing_port(db: Session, port_id: int=0, values: Dict={}, updated_by: int=0):
    values = process_schema_dictionary(info=values)
    values['updated_by'] = updated_by
    update_port(db=db, id=port_id, values=values)
    return {
        'status': True,
        'message': 'Success',
    }

def delete_existing_port_type(db: Session, port_type_id: int=0):
    delete_port_type(db=db, id=port_type_id)
    return {
        'status': True,
        'message': 'Success',
    }

def delete_existing_port(db: Session, port_id: int=0):
    delete_port(db=db, id=port_id)
    return {
        'status': True,
        'message': 'Success',
    }

def retrieve_port_types(db: Session):
    data = get_all_port_types(db=db)
    return paginate(data)

def retrieve_ports(db: Session):
    data = get_all_ports(db=db)
    return paginate(data)

def retrieve_ports_by_room(db: Session, room_id: int=0):
    data = get_all_ports_by_room_id(db=db, room_id=room_id)
    return paginate(data)

def retrieve_ports_by_control_box(db: Session, control_box_id: int=0):
    data = get_all_ports_by_control_box_id(db=db, control_box_id=control_box_id)
    return paginate(data)

def retrieve_ports_by_port_type(db: Session, port_type_id: int=0):
    data = get_all_ports_by_port_type_id(db=db, port_type_id=port_type_id)
    return paginate(data)

def retrieve_ports_by_control_box_and_port_type(db: Session, control_box_id: int=0, port_type_id: int=0):
    data = get_all_ports_by_control_box_id_and_port_type_id(db=db, control_box_id=control_box_id, port_type_id=port_type_id)
    return paginate(data)

def retrieve_ports_by_room_and_port_type(db: Session, room_id: int=0, port_type_id: int=0):
    data = get_all_ports_by_room_id_and_port_type_id(db=db, room_id=room_id, port_type_id=port_type_id)
    return paginate(data)

def retrieve_single_port_type(db: Session, port_type_id: int=0):
    port_type = get_port_type_by_id(db=db, id=port_type_id)
    if port_type is None:
        return {
            'status': False,
            'message': 'Not found',
            'data': None,
        }
    else:
        return {
            'status': True,
            'message': 'Success',
            'data': port_type,
        }
    
def retrieve_single_port(db: Session, port_id: int=0):
    port = get_port_by_id(db=db, id=port_id)
    if port is None:
        return {
            'status': False,
            'message': 'Not found',
            'data': None,
        }
    else:
        return {
            'status': True,
            'message': 'Success',
            'data': port,
        }