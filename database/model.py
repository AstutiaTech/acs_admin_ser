from models.admins import Admin, create_admin, update_admin, get_all_admin, get_admin_by_id, get_admin_by_email, get_admin_by_username, admin_login, count_admins
from models.asset_types import Asset_Type, create_asset_type, update_asset_type, delete_asset_type, get_all_asset_types, get_asset_type_by_id, count_asset_types
from models.asset_files import Asset_File, create_asset_file, update_asset_file, delete_asset_file, get_all_asset_files, get_all_asset_files_by_asset_id, get_asset_file_by_id, count_asset_files, count_asset_files_by_asset_id
from models.assets import Asset, create_asset, update_asset, delete_asset, get_all_assets, get_all_assets_paginated, get_all_assets_paginated_with_files, get_assets_by_owner_id, get_assets_by_owner_id_with_files, get_assets_by_asset_type_id, get_assets_by_asset_type_id_with_files, get_assets_by_owner_id_and_asset_type_id, get_assets_by_owner_id_and_asset_type_id_with_files, get_asset_by_id, get_asset_by_id_with_files, count_assets
from models.auth_tokens import Auth_Token, create_auth_token, update_auth_token, ping_auth_token, get_auth_token_by_id, get_auth_token_by_token, get_auth_token_by_user_id, get_auth_token_by_admin_id, get_last_login_auth_token_by_user_id, get_last_login_auth_token_by_admin_id
from models.batteries import Battery, create_battery, update_battery, delete_battery, get_all_batteries, get_all_batteries_by_control_box_id, get_battery_by_id, count_batteries, count_batteries_by_control_box_id
from models.control_boxes import Control_Box, create_control_box, update_control_box, delete_control_box, get_all_control_boxes, get_all_control_boxes_by_asset_id, get_control_box_by_id, count_control_boxes, count_control_boxes_by_asset_id
from models.inverters import Inverter, create_inverter, update_inverter, delete_inverter, get_all_inverters, get_all_inverters_by_control_box_id, get_inverter_by_id, count_inverters, count_inverters_by_control_box_id
from models.logs import Log, create_log, update_log, get_all_logs, get_all_logs_by_asset_id, get_all_logs_by_control_box_id, get_all_logs_by_battery_id, get_all_logs_by_inverter_id, get_all_logs_by_sensor_id, get_all_logs_by_port_id, get_log_by_id, count_logs, count_logs_by_asset_id, count_logs_by_control_box_id, count_logs_by_battery_id, count_logs_by_inverter_id, count_logs_by_sensor_id, count_logs_by_port_id
from models.owners import Owner, create_owner, update_owner, get_all_owners, get_all_owners_paginated, get_all_owners_by_status_paginated, search_owners, get_owner_by_id, count_owners
from models.port_types import Port_Type, create_port_type, update_port_type, delete_port_type, get_all_port_types, get_port_type_by_id, count_port_types
from models.ports import Port, create_port, update_port, delete_port, get_all_ports, get_all_ports_by_room_id, get_all_ports_by_control_box_id, get_all_ports_by_port_type_id, get_all_ports_by_room_id_and_port_type_id, get_all_ports_by_control_box_id_and_port_type_id, get_port_by_id, count_ports, count_ports_by_room_id, count_ports_by_control_box_id, count_ports_by_port_type_id
from models.room_types import Room_Type, create_room_type, update_room_type, delete_room_type, get_all_room_types, get_room_type_by_id, count_room_types
from models.rooms import Room, create_room, update_room, delete_room, get_all_rooms, get_all_rooms_by_asset_id, get_all_rooms_by_room_type_id, get_all_rooms_by_asset_id_and_room_type_id, get_all_rooms_by_control_box_id, get_all_rooms_by_control_box_id_and_room_type_id, get_room_by_id, count_rooms, count_rooms_by_asset_id, count_rooms_by_room_type_id, count_rooms_by_asset_id_and_room_type_id, count_rooms_by_control_box_id
from models.sensors import Sensor, create_sensor, update_sensor, delete_sensor, get_all_sensors, get_all_sensors_by_control_box_id, get_sensor_by_id, count_sensors, count_sensors_by_control_box_id
from models.users import User, create_user, update_user, get_all_users, get_all_users_paginated, get_users_by_owner_id, get_users_by_owner_id_and_status, get_user_by_id, get_user_by_email, get_user_by_username, search_user, user_login, count_users, count_user_by_email, count_user_by_username
import string
import random
from sqlalchemy.orm import Session

def id_generator(size=15, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def admin_registration_unique_field_check(db: Session, username: str=None, email: str=None):
    username_check = get_admin_by_username(db=db, username=username)
    email_check = get_admin_by_email(db=db, email=email)
    if username_check is not None:
        return {
            'status': False,
            'message': 'Username already exist',
        }
    elif email_check is not None:
        return {
            'status': False,
            'message': 'Email already exist'
        }
    else:
        return {
            'status': True,
            'message': 'Validation successful'
        }
    
def user_registration_unique_field_check(db: Session, username: str=None, email: str=None):
    username_check = get_user_by_username(db=db, username=username)
    email_check = get_user_by_email(db=db, email=email)
    if username_check is not None:
        return {
            'status': False,
            'message': 'Username already exist',
        }
    elif email_check is not None:
        return {
            'status': False,
            'message': 'Email already exist'
        }
    else:
        return {
            'status': True,
            'message': 'Validation successful'
        }
