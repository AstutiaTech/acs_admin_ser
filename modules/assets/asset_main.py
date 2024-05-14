from typing import Dict
from database.model import create_asset, create_asset_file, update_asset, update_asset_file, delete_asset, delete_asset_file, get_all_assets_paginated, get_all_assets_paginated_with_files, get_assets_by_owner_id, get_assets_by_owner_id_with_files, get_all_asset_files, get_all_asset_files_by_asset_id, get_asset_by_id, get_asset_by_id_with_files, get_asset_file_by_id
from sqlalchemy.orm import Session
from fastapi import UploadFile
from fastapi_pagination.ext.sqlalchemy import paginate
from modules.utils.tools import process_schema_dictionary, generate_basic_reference
from modules.utils.net import cloudinary_upload_file, cloudinary_upload_base64

def insert_new_asset(db: Session, owner_id: int=0, asset_type: int=0, name: str=None, description: str=None, address: str=None, city: str=None, state: str=None, country: str=None, latitude: str=None, longitude: str=None):
    reference = generate_basic_reference()
    asset = create_asset(db=db, owner_id=owner_id, reference=reference, asset_type=asset_type, name=name, description=description, address=address, city=city, state=state, country=country, latitude=latitude, longitude=longitude, status=1)
    return {
        'status': True,
        'message': 'Success',
        'data': asset,
    }

def update_existing_asset(db: Session, asset_id: int=0, values: Dict={}):
    values = process_schema_dictionary(info=values)
    update_asset(db=db, id=asset_id, values=values)
    return {
        'status': True,
        'message': 'Success',
    }

def insert_new_asset_file_form_data(db: Session, uploaded_file: UploadFile, asset_id: int=0, file_type: int=0):
    upfile = cloudinary_upload_file(image=uploaded_file)
    if upfile['status'] == False:
        return {
            'status': False,
            'message': 'Asset file creation: ' + str(upfile['message']),
            'data': None
        }
    else:
        file_url = upfile['data']
        asset_file = create_asset_file(db=db, asset_id=asset_id, file_type=file_type, file_url=file_url, status=1)
        return {
            'status': True,
            'message': 'Success',
            'data': asset_file
        }
    
def insert_new_asset_file_base64(db: Session, base64_str: str, asset_id: int=0, file_type: int=0):
    upfile = cloudinary_upload_base64(base64_str=base64_str)
    if upfile['status'] == False:
        return {
            'status': False,
            'message': 'Asset file creation: ' + str(upfile['message']),
            'data': None
        }
    else:
        file_url = upfile['data']
        asset_file = create_asset_file(db=db, asset_id=asset_id, file_type=file_type, file_url=file_url, status=1)
        return {
            'status': True,
            'message': 'Success',
            'data': asset_file
        }
    
def update_existing_asset_file_form_data(db: Session, file_id: int, uploaded_file: UploadFile=None, status: int=None):
    values = {}
    if uploaded_file is None:
        if status is not None:
            values['status'] = status
        update_asset_file(db=db, id=file_id, values=values)
        return {
            'status': True,
            'message': 'Success',
        }
    else:
        upfile = cloudinary_upload_file(image=uploaded_file)
        if upfile['status'] == False:
            return {
                'status': False,
                'message': 'Asset file creation: ' + str(upfile['message']),
            }
        else:
            values['file_url'] = upfile['data']
            if status is not None:
                values['status'] = status
            update_asset_file(db=db, id=file_id, values=values)
            return {
                'status': True,
                'message': 'Success',
            }

def update_existing_asset_file_base64(db: Session, file_id: int, base64_str: str=None, status: int=None):
    values = {}
    if base64_str is None:
        if status is not None:
            values['status'] = status
        update_asset_file(db=db, id=file_id, values=values)
        return {
            'status': True,
            'message': 'Success',
        }
    else:
        upfile = cloudinary_upload_base64(base64_str=base64_str)
        if upfile['status'] == False:
            return {
                'status': False,
                'message': 'Asset file creation: ' + str(upfile['message']),
            }
        else:
            values['file_url'] = upfile['data']
            if status is not None:
                values['status'] = status
            update_asset_file(db=db, id=file_id, values=values)
            return {
                'status': True,
                'message': 'Success',
            }
        
def delete_existing_asset(db: Session, asset_id: int=0):
    delete_asset(db=db, id=asset_id)
    return {
        'status': True,
        'message': 'Success',
    }

def delete_existing_asset_file(db: Session, file_id: int=0):
    delete_asset_file(db=db, id=file_id)
    return {
        'status': True,
        'message': 'Success',
    }

def retrieve_assets(db: Session):
    data = get_all_assets_paginated(db=db)
    return paginate(data)

def retrieve_assets_with_files(db: Session):
    data = get_all_assets_paginated_with_files(db=db)
    return paginate(data)

def retrieve_assets_by_owners(db: Session, owner_id: int=0):
    data = get_assets_by_owner_id(db=db, owner_id=owner_id)
    return paginate(data)

def retrieve_assets_by_owners_with_files(db: Session, owner_id: int=0):
    data = get_assets_by_owner_id_with_files(db=db, owner_id=owner_id)
    return paginate(data)

def retrieve_single_asset(db: Session, asset_id: int=0):
    asset = get_asset_by_id(db=db, id=asset_id)
    if asset is None:
        return {
            'status': False,
            'message': 'Not found',
            'data': None
        }
    else:
        return {
            'status': True,
            'message': 'Success',
            'data': asset
        }
    
def retrieve_single_asset_with_files(db: Session, asset_id: int=0):
    asset = get_asset_by_id_with_files(db=db, id=asset_id)
    if asset is None:
        return {
            'status': False,
            'message': 'Not found',
            'data': None
        }
    else:
        return {
            'status': True,
            'message': 'Success',
            'data': asset
        }
    
def retrieve_all_asset_files(db: Session):
    data = get_all_asset_files(db=db)
    return paginate(data)

def retrieve_all_asset_files_by_asset(db: Session, asset_id: int=0):
    data = get_all_asset_files_by_asset_id(db=db, asset_id=asset_id)
    return paginate(data)

def retrieve_single_asset_file(db: Session, file_id: int=0):
    asset_file = get_asset_file_by_id(db=db, id=file_id)
    if asset_file is None:
        return {
            'status': False,
            'message': 'Not found',
            'data': None
        }
    else:
        return {
            'status': True,
            'message': 'Success',
            'data': asset_file
        }