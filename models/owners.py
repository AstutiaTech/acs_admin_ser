from email.policy import default
from typing import Dict
from sqlalchemy import Column, Integer, String, DateTime, BigInteger, DECIMAL, Float, TIMESTAMP, SmallInteger, Text, desc
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import and_, or_
from sqlalchemy.sql.schema import ForeignKey
from database.db import Base, get_laravel_datetime
import decimal


class Owner(Base):

    __tablename__ = "owners"
     
    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String, nullable=True)
    description = Column(String, nullable=True)
    status = Column(SmallInteger, default=0)
    created_at = Column(TIMESTAMP(timezone=True), nullable=True)
    updated_at = Column(TIMESTAMP(timezone=True), nullable=True)
    deleted_at = Column(TIMESTAMP(timezone=True), nullable=True)


def create_owner(db: Session, name: str=None, description: str=None, status: int=0):
    owner = Owner(name=name, description=description, status=status, created_at=get_laravel_datetime(), updated_at=get_laravel_datetime())
    db.add(owner)
    db.commit()
    db.refresh(owner)
    return owner

def update_owner(db: Session, id: int=0, values: Dict={}):
    values['updated_at'] = get_laravel_datetime()
    db.query(Owner).filter_by(id=id).update(values)
    db.commit()
    return True

def get_all_owners(db: Session):
    return db.query(Owner).filter(Owner.deleted_at == None).order_by(desc(Owner.created_at)).all()

def get_owner_by_id(db: Session, id: int=0):
    return db.query(Owner).filter_by(id=id).first()
    
def count_owners(db: Session):
    return db.query(Owner).filter(Owner.deleted_at == None).order_by(desc(Owner.created_at)).count()
    
