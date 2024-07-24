from email.policy import default
from typing import Dict
from sqlalchemy import Column, Integer, String, DateTime, BigInteger, DECIMAL, Float, TIMESTAMP, SmallInteger, Text, desc
from sqlalchemy.orm import Session, relationship
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import and_, or_
from sqlalchemy.sql.schema import ForeignKey
from database.db import Base, get_laravel_datetime
import decimal


class Room(Base):

    __tablename__ = "rooms"
     
    id = Column(BigInteger, primary_key=True, index=True)
    asset_id = Column(BigInteger, default=0)
    room_type_id = Column(BigInteger, default=0)
    control_box_id = Column(BigInteger, default=0)
    name = Column(String, nullable=True)
    description = Column(Text, nullable=True)
    status = Column(SmallInteger, default=0)
    created_by = Column(BigInteger, default=0)
    updated_by = Column(BigInteger, default=0)
    created_at = Column(TIMESTAMP(timezone=True), nullable=True)
    updated_at = Column(TIMESTAMP(timezone=True), nullable=True)
    deleted_at = Column(TIMESTAMP(timezone=True), nullable=True)


def create_room(db: Session, asset_id: int=0, room_type_id: int=0, control_box_id: int=0, name: str=None, description: str=None, status: int=0, created_by: int=0, updated_by: int=0):
    room = Room(asset_id=asset_id, room_type_id=room_type_id, control_box_id=control_box_id, name=name, description=description, status=status, created_by=created_by, updated_by=updated_by, created_at=get_laravel_datetime(), updated_at=get_laravel_datetime())
    db.add(room)
    db.commit()
    db.refresh(room)
    return room

def update_room(db: Session, id: int=0, values: Dict={}):
    values['updated_at'] = get_laravel_datetime()
    db.query(Room).filter_by(id=id).update(values)
    db.commit()
    return True

def delete_room(db: Session, id: int=0):
    values = {
        'deleted_at': get_laravel_datetime(),
    }
    db.query(Room).filter_by(id=id).update(values)
    db.commit()
    return True

def get_all_rooms(db: Session):
    return db.query(Room).filter(Room.deleted_at == None).order_by(desc(Room.created_at))

def get_all_rooms_by_asset_id(db: Session, asset_id: int=0):
    return db.query(Room).filter(and_(Room.asset_id == asset_id, Room.deleted_at == None)).order_by(desc(Room.created_at))

def get_all_rooms_by_room_type_id(db: Session, room_type_id: int=0):
    return db.query(Room).filter(and_(Room.room_type_id == room_type_id, Room.deleted_at == None)).order_by(desc(Room.created_at))

def get_all_rooms_by_asset_id_and_room_type_id(db: Session, asset_id: int=0, room_type_id: int=0):
    return db.query(Room).filter(and_(Room.asset_id == asset_id, Room.room_type_id == room_type_id, Room.deleted_at == None)).order_by(desc(Room.created_at))

def get_all_rooms_by_control_box_id(db: Session, control_box_id: int=0):
    return db.query(Room).filter(and_(Room.control_box_id == control_box_id, Room.deleted_at == None)).order_by(desc(Room.created_at))

def get_all_rooms_by_control_box_id_and_room_type_id(db: Session, control_box_id: int=0, room_type_id: int=0):
    return db.query(Room).filter(and_(Room.control_box_id == control_box_id, Room.room_type_id == room_type_id, Room.deleted_at == None)).order_by(desc(Room.created_at))

def get_room_by_id(db: Session, id: int=0):
    return db.query(Room).filter_by(id=id).first()
    
def count_rooms(db: Session):
    return db.query(Room).filter(Room.deleted_at == None).count()

def count_rooms_by_asset_id(db: Session, asset_id: int=0):
    return db.query(Room).filter(and_(Room.asset_id == asset_id, Room.deleted_at == None)).count()

def count_rooms_by_room_type_id(db: Session, room_type_id: int=0):
    return db.query(Room).filter(and_(Room.room_type_id == room_type_id, Room.deleted_at == None)).count()

def count_rooms_by_asset_id_and_room_type_id(db: Session, asset_id: int=0, room_type_id: int=0):
    return db.query(Room).filter(and_(Room.asset_id == asset_id, Room.room_type_id == room_type_id, Room.deleted_at == None)).count()

def count_rooms_by_control_box_id(db: Session, control_box_id: int=0):
    return db.query(Room).filter(and_(Room.control_box_id == control_box_id, Room.deleted_at == None)).count()
