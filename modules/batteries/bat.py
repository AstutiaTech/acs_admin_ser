from typing import Dict
from database.model import create_battery, update_battery, delete_battery, get_all_batteries, get_all_batteries_by_control_box_id, get_battery_by_id
from sqlalchemy.orm import Session
from fastapi_pagination.ext.sqlalchemy import paginate
from modules.utils.tools import process_schema_dictionary, generate_basic_reference

def insert_new_battery(db:Session, control_box_id: int=0, state_of_charge: str=None, current_drawn: str=None, voltage: str=None, capacity: str=None):
    reference = generate_basic_reference()
    battery = create_battery(db=db, control_box_id=control_box_id, reference=reference, state_of_charge=state_of_charge, current_drawn=current_drawn, voltage=voltage, capacity=capacity, status=0)
    return {
        'status': True,
        'message': 'Success',
        'data': battery,
    }

def update_existing_battery(db: Session, battery_id: int=0, values: Dict={}):
    values = process_schema_dictionary(info=values)
    update_battery(db=db, id=battery_id, values=values)
    return {
        'status': True,
        'message': 'Success',
    }

def delete_existing_battery(db: Session, battery_id: int=0):
    delete_battery(db=db, id=battery_id)
    return {
        'status': True,
        'message': 'Success',
    }

def retrieve_batteries(db: Session):
    data = get_all_batteries(db=db)
    return paginate(data)

def retrieve_batteries_by_control_box(db: Session, control_box_id: int=0):
    data = get_all_batteries_by_control_box_id(db=db, control_box_id=control_box_id)
    return paginate(data)

def retrieve_single_battery(db: Session, battery_id: int=0):
    battery = get_battery_by_id(db=db, id=battery_id)
    if battery is None:
        return {
            'status': False,
            'message': 'Not found',
            'data': None,
        }
    else:
        return {
            'status': True,
            'message': 'Success',
            'data': battery,
        }