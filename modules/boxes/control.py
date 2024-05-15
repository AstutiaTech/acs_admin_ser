from typing import Dict
from database.model import create_control_box, update_control_box, delete_control_box, get_all_control_boxes, get_all_control_boxes_by_asset_id, get_control_box_by_id
from sqlalchemy.orm import Session
from fastapi_pagination.ext.sqlalchemy import paginate
from modules.utils.tools import process_schema_dictionary, generate_basic_reference

def insert_control_box(db: Session, asset_id: int=0, private_key: str=None, comms_sim_card_value: str=None, comms_sim_card_number: str=None, comms_wifi_provider: str=None):
    reference = generate_basic_reference()
    control_box = create_control_box(db=db, asset_id=asset_id, reference=reference, private_key=private_key, comms_sim_card_value=comms_sim_card_value, comms_sim_card_number=comms_sim_card_number, comms_wifi_provider=comms_wifi_provider, status=1)
    return {
        'status': True,
        'message': 'Success',
        'data': control_box,
    }

def update_existing_control_box(db: Session, control_box_id: int=0, values: Dict={}):
    values = process_schema_dictionary(info=values)
    update_control_box(db=db, id=control_box_id, values=values)
    return {
        'status': True,
        'message': 'Success',
    }

def delete_existing_control_box(db: Session, control_box_id: int=0):
    delete_control_box(db=db, id=control_box_id)
    return {
        'status': True,
        'message': 'Success',
    }

def retrieve_all_control_boxes(db: Session):
    data = get_all_control_boxes(db=db)
    return paginate(data)

def retrieve_control_boxes_by_asset(db: Session, asset_id: int=0):
    data = get_all_control_boxes_by_asset_id(db=db, asset_id=asset_id)
    return paginate(data)

def retrieve_single_control_box(db: Session, control_box_id: int=0):
    control_box = get_control_box_by_id(db=db, id=control_box_id)
    if control_box is None:
        return {
            'status': False,
            'message': 'Not found',
            'data': None,
        }
    else:
        return {
            'status': True,
            'message': 'Success',
            'data': control_box,
        }