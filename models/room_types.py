from email.policy import default
from typing import Dict
from sqlalchemy import Column, Integer, String, DateTime, BigInteger, DECIMAL, Float, TIMESTAMP, SmallInteger, Text, desc
from sqlalchemy.orm import Session, relationship
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import and_, or_
from sqlalchemy.sql.schema import ForeignKey
from database.db import Base, get_laravel_datetime
import decimal


class Room_Type(Base):

    __tablename__ = "room_types"
     
    id = Column(BigInteger, primary_key=True, index=True)
    asset_type_id = Column(BigInteger, default=0)
    name = Column(String, nullable=True)
    description = Column(Text, nullable=True)
    file_url = Column(Text, nullable=True)
    slug = Column(String, nullable=True)
    value_code = Column(String, nullable=True)
    status = Column(SmallInteger, default=0)
    created_by = Column(BigInteger, default=0)
    updated_by = Column(BigInteger, default=0)
    created_at = Column(TIMESTAMP(timezone=True), nullable=True)
    updated_at = Column(TIMESTAMP(timezone=True), nullable=True)
    deleted_at = Column(TIMESTAMP(timezone=True), nullable=True)


def create_room_type(db: Session, asset_type_id: int=0, name: str=None, description: str=None, file_url: str=None, slug: str=None, value_code: str=None, status: int=0, created_by: int=0, updated_by: int=0):
    room_type = Room_Type(asset_type_id=asset_type_id, name=name, description=description, file_url=file_url, slug=slug, value_code=value_code, status=status, created_by=created_by, updated_by=updated_by, created_at=get_laravel_datetime(), updated_at=get_laravel_datetime())
    db.add(room_type)
    db.commit()
    db.refresh(room_type)
    return room_type

def update_room_type(db: Session, id: int=0, values: Dict={}):
    values['updated_at'] = get_laravel_datetime()
    db.query(Room_Type).filter_by(id=id).update(values)
    db.commit()
    return True

def delete_room_type(db: Session, id: int=0):
    values = {
        'deleted_at': get_laravel_datetime(),
    }
    db.query(Room_Type).filter_by(id=id).update(values)
    db.commit()
    return True

def get_all_room_types(db: Session):
    return db.query(Room_Type).filter(Room_Type.deleted_at == None).order_by(desc(Room_Type.created_at))

def get_room_type_by_id(db: Session, id: int=0):
    return db.query(Room_Type).filter_by(id=id).first()
    
def count_room_types(db: Session):
    return db.query(Room_Type).filter(Room_Type.deleted_at == None).count()
