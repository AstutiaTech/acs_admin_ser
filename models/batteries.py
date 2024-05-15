from email.policy import default
from typing import Dict
from sqlalchemy import Column, Integer, String, DateTime, BigInteger, DECIMAL, Float, TIMESTAMP, SmallInteger, Text
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import and_, or_
from sqlalchemy.sql.schema import ForeignKey
from database.db import Base, get_laravel_datetime
import decimal


class Battery(Base):

    __tablename__ = "batteries"
     
    id = Column(BigInteger, primary_key=True, index=True)
    control_box_id = Column(BigInteger, default=0)
    reference = Column(String, nullable=True)
    state_of_charge = Column(String, nullable=True)
    current_drawn = Column(String, nullable=True)
    voltage = Column(String, nullable=True)
    capacity = Column(String, nullable=True)
    status = Column(SmallInteger, default=0)
    created_at = Column(TIMESTAMP(timezone=True), nullable=True)
    updated_at = Column(TIMESTAMP(timezone=True), nullable=True)
    deleted_at = Column(TIMESTAMP(timezone=True), nullable=True)


def create_battery(db: Session, control_box_id: int=0, reference: str=None, state_of_charge: str=None, current_drawn: str=None, voltage: str=None, capacity: str=None, status: int=0):
    battery = Battery(control_box_id=control_box_id, reference=reference, state_of_charge=state_of_charge, current_drawn=current_drawn, voltage=voltage, capacity=capacity, status=status, created_at=get_laravel_datetime(), updated_at=get_laravel_datetime())
    db.add(battery)
    db.commit()
    db.refresh(battery)
    return battery

def update_battery(db: Session, id: int=0, values: Dict={}):
    values['updated_at'] = get_laravel_datetime()
    db.query(Battery).filter_by(id=id).update(values)
    db.commit()
    return True

def delete_battery(db: Session, id: int=0):
    values = {
        'deleted_at': get_laravel_datetime(),
    }
    db.query(Battery).filter_by(id=id).update(values)
    db.commit()
    return True

def get_all_batteries(db: Session):
    return db.query(Battery).filter(Battery.deleted_at == None)

def get_all_batteries_by_control_box_id(db: Session, control_box_id: int=0):
    return db.query(Battery).filter(and_(Battery.control_box_id == control_box_id, Battery.deleted_at == None))

def get_battery_by_id(db: Session, id: int=0):
    return db.query(Battery).filter_by(id=id).first()
    
def count_batteries(db: Session):
    return db.query(Battery).filter(Battery.deleted_at == None).count()

def count_batteries_by_control_box_id(db: Session, control_box_id: int=0):
    return db.query(Battery).filter(and_(Battery.control_box_id == control_box_id, Battery.deleted_at == None)).count()
