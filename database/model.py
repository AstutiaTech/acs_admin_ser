from models.users import User, create_user, update_user, get_all_users, get_user_by_id, get_user_by_email, get_user_by_username, get_user_by_phone_number, user_login, count_users, count_user_by_email, count_user_by_username, count_user_by_phone_number
import string
import random
from sqlalchemy.orm import Session

def id_generator(size=15, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
