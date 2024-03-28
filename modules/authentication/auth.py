from typing import Dict
from database.model import admin_login, create_admin, update_admin, admin_registration_unique_field_check, get_admin_by_id
from modules.utils.net import get_ip_info, process_phone_number
from modules.utils.tools import process_schema_dictionary
from modules.utils.auth import AuthHandler, get_next_few_minutes, check_if_time_as_pass_now
from sqlalchemy.orm import Session
import random
import datetime
import random

auth = AuthHandler()
  
def login_admin(db: Session, field: str=None, password: str=None):
    admin = admin_login(db=db, field=field)
    return admin
    if admin is None:
        return {
            'status': False,
            'message': 'Username or Email not found',
            'data': None,
        }
    else:
        if not auth.verify_password(plain_password=password, hashed_password=admin.password):
            return {
                'status': False,
                'message': 'Incorrect Password',
                'data': None,
            }
        else:
            if admin.status == 0:
                return {
                    'status': False,
                    'message': 'Admin has been deactivated',
                    'data': None,
                }
            else:
                if admin.deleted_at is not None:
                    return {
                        'status': False,
                        'message': 'Admin has been deleted',
                        'data': None,
                    }
                else:
                    payload = {
                        'id': admin.id,
                        'username': admin.username,
                        'email': admin.email,
                        'role_id': admin.role,
                    }
                    token = auth.encode_token(user=payload)
                    data = {
                        'access_token': token,
                        'id': admin.id,
                        'username': admin.username,
                        'email': admin.email,
                        'first_name': admin.first_name,
                        'last_name': admin.last_name,
                        'role': admin.role,
                        'created_at': admin.created_at,
                    }
                    return {
                        'status': True,
                        'message': 'Login Success',
                        'data': data,
                    }

def register_admin(db: Session, role: int = 0, username: str = None, email: str = None, password: str = None, created_by: int=0):
    check = admin_registration_unique_field_check(db=db, username=username, email=email)
    if check['status'] == False:
        return {
            'status': False,
            'message': check['message'],
            'data': None,
        }
    else:
        hashed_password = auth.get_password_hash(password=password)
        admin = create_admin(db=db, role=role, email=email, username=username, password=hashed_password, status=1, created_by=created_by)
        data = {
            'id': admin.id,
            'username': admin.username,
            'email': admin.email,
            'first_name': admin.first_name,
            'last_name': admin.last_name,
            'role': admin.role,
            'created_at': admin.created_at,
        }
        return {
            'status': True,
            'message': 'Success',
            'data': data,
        }
    
def get_loggedin_admin(db: Session, admin_id: str=None):
    admin = get_admin_by_id(db=db, id=admin_id)
    if admin is None:
        return {
            'status': False,
            'message': 'Admin not found',
            'data': None
        }
    else:
        data = {
            'id': admin.id,
            'username': admin.username,
            'email': admin.email,
            'first_name': admin.first_name,
            'last_name': admin.last_name,
            'role': admin.role,
            'created_at': admin.created_at,
        }
        return {
            'status': True,
            'message': 'Success',
            'data': data,
        }
    
def update_admin_details(db: Session, admin_id: int=0, values: Dict={}, updated_by: int=0):
    values = process_schema_dictionary(info=values)
    if updated_by != admin_id:
        values['updated_by'] = updated_by
    update_admin(db=db, id=admin_id, values=values)
    return {
        'status': True,
        'message': 'Success'
    }

def update_admin_password(db: Session, admin_id: int=0, password: str=None, password_confirmation: str=None, old_password: str = None):
    admin_info = get_admin_by_id(db=db, id=admin_id)
    if admin_info is None:
        return {
            'status': False,
            'message': 'Not found'
        }
    else:
        if password != password_confirmation:
            return {
                'status': False,
                'message': 'Password not equal with confirm password',
            }
        else:
            if auth.verify_password(plain_password=old_password, hashed_password=admin_info.password) == True:
                password = auth.get_password_hash(password=password)
                da = {
                    'password': password
                }
                update_admin(db=db, id=admin_id, values=da)
                return {
                    'status': True,
                    'message': 'Success'
                }
            else:
                return {
                    'status': False,
                    'message': 'Old Password Incorrect'
                }
