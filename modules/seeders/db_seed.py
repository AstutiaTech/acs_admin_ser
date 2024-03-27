from sqlalchemy.orm import Session
from modules.seeders.admin import seed_admin

def run_seed(db: Session):
    seed_admin(db=db)
    return True