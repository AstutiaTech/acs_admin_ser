from sqlalchemy.orm import Session
from modules.authentication.auth import register_admin

seed = [
    {
        'role': 1,
        'email': 'superadmin@acs.com',
        'username': 'superadmin',
        'password': 'secret',
        'created_by': 1,
    },
]

def seed_admin(db: Session):
    global seed
    if len(seed) > 0:
        for i in range(len(seed)):
            register_admin(db=db, role=seed[i]['role'], username=seed[i]['username'], email=seed[i]['email'], password=seed[i]['password'], created_by=seed[i]['created_by'])
    return True
