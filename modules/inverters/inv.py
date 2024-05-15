from typing import Dict
from database.model import create_inverter, update_inverter, delete_inverter, get_all_inverters, get_all_inverters_by_control_box_id, get_inverter_by_id
from sqlalchemy.orm import Session
from fastapi_pagination.ext.sqlalchemy import paginate
from modules.utils.tools import process_schema_dictionary, generate_basic_reference

def insert_new_inverter(db: Session, control_box_id: int=0, capacity: str=None, voltage_input: str=None, voltage_output: str=None):
    reference = generate_basic_reference()
    inverter = create_inverter(db=db, control_box_id=control_box_id, reference=reference, voltage_input=voltage_input, voltage_output=voltage_output, capacity=capacity, status=0)
    return {
        'status': True,
        'message': 'Success',
        'data': inverter,
    }

def update_existing_inverter(db: Session, inverter_id: int=0, values: Dict={}):
    values = process_schema_dictionary(info=values)
    update_inverter(db=db, id=inverter_id, values=values)
    return {
        'status': True,
        'message': 'Success',
    }

def delete_existing_inverter(db: Session, inverter_id: int=0):
    delete_inverter(db=db, id=inverter_id)
    return {
        'status': True,
        'message': 'Success',
    }

def retrieve_inverters(db: Session):
    data = get_all_inverters(db=db)
    return paginate(data)

def retrieve_inverters_by_control_box(db: Session, control_box_id: int=0):
    data = get_all_inverters_by_control_box_id(db=db, control_box_id=control_box_id)
    return paginate(data)

def retrieve_single_inverter(db: Session, inverter_id: int=0):
    inverter = get_inverter_by_id(db=db, id=inverter_id)
    if inverter is None:
        return {
            'status': False,
            'message': 'Not found',
            'data': None,
        }
    else:
        return {
            'status': True,
            'message': 'Success',
            'data': inverter,
        }