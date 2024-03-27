from fastapi import APIRouter, Depends, Request
from modules.seeders.db_seed import run_seed
from database.db import get_session
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/seeder",
    tags=["seeder"]
)

@router.get("/run")
async def run(request: Request, db: Session = Depends(get_session)):
    return run_seed(db=db)
    
