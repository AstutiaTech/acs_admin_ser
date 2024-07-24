import string 
import random
from datetime import datetime
from typing import List, Dict
from settings.config import load_env_config
import dateparser
import time
import re

config = load_env_config()

def rand_string_generator(size=10):
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(size))

def rand_upper_string_generator(size=10):
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(size))
    
def rand_lower_string_generator(size=10):
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(size))

def generate_transaction_reference(tran_type: str = None, rand_type: int = 1, rand_size: int = 10):
    dt = datetime.now()
    ts = datetime.timestamp(dt)
    ts = int(ts)
    if rand_type == 1:
        return str(tran_type).upper() + "_" + rand_string_generator(size=rand_size) + "_" + str(ts)
    elif rand_type == 2:
        return str(tran_type).upper() + "_" + rand_upper_string_generator(size=rand_size) + "_" + str(ts)
    elif rand_type == 3:
        return str(tran_type).upper() + "_" + rand_lower_string_generator(size=rand_size) + "_" + str(ts)

def generate_basic_reference(rand_size: int=10):
    dt = datetime.now()
    ts = datetime.timestamp(dt)
    ts = int(ts)
    return rand_upper_string_generator(size=rand_size) + "_" + str(ts)

def process_schema_dictionary(info: Dict={}):
    if bool(info) == False:
        return {}
    else:
        retval = {}
        for i in info:
            if info[i] != None:
                retval[i] = info[i]
        return retval
    
def generate_host_id(first_char: str=None, number: int=0):
    # return first_char + str(number).zfill(9)
    return first_char + rand_upper_string_generator(size=number)

def generate_battery_code(number: int=0, length: int=0):
    return "A87" + str(number).zfill(length) + "P"

def process_datetime_string(time_str: str = None):
    if time_str is None:
        return None
    else:
        return dateparser.parse(str(time_str), date_formats=['%d-%m-%Y %H:%M:%S'])
    
def slugify(input_string: str=None, strip: str='-'):
    if input_string is None:
        return None
    else:
        input_string = input_string.encode('ascii', 'ignore').decode('ascii').lower()
        slug = re.sub(r'[^a-z0-9]+', '-', input_string)
        slug = slug.strip(strip)
        return slug