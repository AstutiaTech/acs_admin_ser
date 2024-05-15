from typing import Dict
from database.model import create_sensor, update_sensor, delete_sensor, get_all_sensors, get_all_sensors_by_control_box_id, get_sensor_by_id
from sqlalchemy.orm import Session
from fastapi_pagination.ext.sqlalchemy import paginate
from modules.utils.tools import process_schema_dictionary, generate_basic_reference

def insert_new_sensor(db: Session, control_box_id: int=0, sensor_type: int=0, voltage_input: str=None, voltage_output: str=None):
    reference = generate_basic_reference()
    sensor = create_sensor(db=db, control_box_id=control_box_id, reference=reference, sensor_type=sensor_type, voltage_input=voltage_input, voltage_output=voltage_output, status=1)
    return {
        'status': True,
        'message': 'Success',
        'data': sensor,
    }

def update_existing_sensor(db: Session, sensor_id: int=0, values: Dict={}):
    values = process_schema_dictionary(info=values)
    update_sensor(db=db, id=sensor_id, values=values)
    return {
        'status': True,
        'message': 'Success',
    }

def delete_existing_sensor(db: Session, sensor_id: int=0):
    delete_sensor(db=db, id=sensor_id)
    return {
        'status': True,
        'message': 'Success',
    }

def retrieve_sensors(db: Session):
    data = get_all_sensors(db=db)
    return paginate(data)

def retrieve_sensors_by_control_box(db: Session, control_box_id: int=0):
    data = get_all_sensors_by_control_box_id(db=db, control_box_id=control_box_id)
    return paginate(data)

def retrieve_single_sensor(db: Session, sensor_id: int=0):
    sensor = get_sensor_by_id(db=db, id=sensor_id)
    if sensor is None:
        return {
            'status': False,
            'message': 'Not found',
            'data': None,
        }
    else:
        return {
            'status': True,
            'message': 'Success',
            'data': sensor,
        }