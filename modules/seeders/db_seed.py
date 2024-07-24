from sqlalchemy.orm import Session
from modules.seeders.admin import seed_admin
from modules.seeders.asset_type import seed_asset_type
from modules.seeders.port_type import seed_port_type
from modules.seeders.room_type import seed_room_type

def run_seed(db: Session):
    seed_admin(db=db)
    seed_asset_type(db=db)
    seed_port_type(db=db)
    seed_room_type(db=db)
    return True