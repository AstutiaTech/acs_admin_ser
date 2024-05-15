from typing import Dict
from database.model import create_port, update_port, delete_port, get_all_ports, get_all_ports_by_control_box_id, get_port_by_id
from sqlalchemy.orm import Session
from fastapi_pagination.ext.sqlalchemy import paginate
from modules.utils.tools import process_schema_dictionary, generate_basic_reference

def insert_new_port(db: Session, control_box_id: int=0, appliance_name: str=None, room_name: str=None, power_rating: str=None, current_drawn: str=None, priority_status: int=0):
    reference = generate_basic_reference()
    port = create_port(db=db, control_box_id=control_box_id, reference=reference, appliance_name=appliance_name, room_name=room_name, power_rating=power_rating, current_drawn=current_drawn, priority_status=priority_status, status=1)
    return {
        'status': True,
        'message': 'Success',
        'data': port,
    }

def update_existing_port(db: Session, port_id: int=0, values: Dict={}):
    values = process_schema_dictionary(info=values)
    update_port(db=db, id=port_id, values=values)
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

def retrieve_ports(db: Session):
    data = get_all_ports(db=db)
    return paginate(data)

def retrieve_ports_by_control_box(db: Session, control_box_id: int=0):
    data = get_all_ports_by_control_box_id(db=db, control_box_id=control_box_id)
    return paginate(data)

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