from typing import Dict
from database.model import create_owner, update_owner, get_all_owners_paginated, get_all_owners_by_status_paginated, search_owners, get_owner_by_id, create_user, update_user, get_all_users_paginated, get_users_by_owner_id, get_users_by_owner_id_and_status, get_user_by_id, search_user, user_registration_unique_field_check
from sqlalchemy.orm import Session
from fastapi_pagination.ext.sqlalchemy import paginate
from modules.utils.tools import process_schema_dictionary
from modules.utils.auth import AuthHandler

auth = AuthHandler()

def insert_new_owner(db: Session, name: str=None, description: str=None):
    owner = create_owner(db=db, name=name, description=description, status=1)
    return {
        'status': True,
        'message': 'Success',
        'data': owner,
    }

def update_existing_owner(db: Session, owner_id: int=0, values: Dict={}):
    values = process_schema_dictionary(info=values)
    update_owner(db=db, id=owner_id, values=values)
    return {
        'status': True,
        'message': 'Success',
    }

def retrieve_owners(db: Session):
    data = get_all_owners_paginated(db=db)
    return paginate(data)

def retrieve_owners_by_status(db: Session, status: int=0):
    data = get_all_owners_by_status_paginated(db=db, status=status)
    return paginate(data)

def retrieve_owners_search(db: Session, query: str=''):
    data = search_owners(db=db, query=query)
    return paginate(data)

def retrieve_single_owner(db: Session, owner_id: int=0):
    owner = get_owner_by_id(db=db, id=owner_id)
    if owner is None:
        return {
            'status': False,
            'message': 'Not found',
            'data': None
        }
    else:
        return {
            'status': True,
            'message': 'Success',
            'data': owner
        }
    
def create_new_user(db: Session, owner_id: int=0, username: str=None, email: str=None, password: str=None, role: int=0):
    check = user_registration_unique_field_check(db=db, username=username, email=email)
    if check['status'] == False:
        return {
            'status': False,
            'message': check['message'],
            'data': None,
        }
    else:
        hashed_password = auth.get_password_hash(password=password)
        hashed_pin = auth.get_password_hash(password="000000")
        user = create_user(db=db, owner_id=owner_id, username=username, email=email, password=hashed_password, pin=hashed_pin, role=role, status=1)
        return {
            'status': True,
            'message': 'Success',
            'data': user,
        }
    
def update_existing_user(db: Session, user_id: int, values: Dict={}):
    values = process_schema_dictionary(info=values)
    if 'password' in values:
        values['password'] = auth.get_password_hash(password=values['password'])
    if 'pin' in values:
        values['pin'] = auth.get_password_hash(password=values['pin'])
    update_user(db=db, id=user_id, values=values)
    return {
        'status': True,
        'message': 'Success'
    }

def retrieve_users(db: Session):
    data = get_all_users_paginated(db=db)
    return paginate(data)

def retrieve_users_by_owners(db: Session, owner_id: int=0):
    data = get_users_by_owner_id(db=db, owner_id=owner_id)
    return paginate(data)

def retrieve_users_by_owners_and_status(db: Session, owner_id: int=0, status: int=0):
    data = get_users_by_owner_id_and_status(db=db, owner_id=owner_id, status=status)
    return paginate(data)

def retrieve_users_search(db: Session, query: str=''):
    data = search_user(db=db, query=query)
    return paginate(data)

def retrieve_single_user(db: Session, user_id: int=0):
    user = get_user_by_id(db=db, id=user_id)
    if user is None:
        return {
            'status': False,
            'message': 'Not found',
            'data': None
        }
    else:
        return {
            'status': True,
            'message': 'Success',
            'data': user
        }
    
