from email.policy import default
from typing import Dict
from sqlalchemy import Column, Integer, String, DateTime, BigInteger, DECIMAL, Float, TIMESTAMP, SmallInteger, Text
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import and_, or_
from sqlalchemy.sql.schema import ForeignKey
from database.db import Base, get_laravel_datetime
import decimal


class Inverter(Base):

    __tablename__ = "inverters"
     
    id = Column(BigInteger, primary_key=True, index=True)
    control_box_id = Column(BigInteger, default=0)
    reference = Column(String, nullable=True)
    capacity = Column(String, nullable=True)
    voltage_input = Column(String, nullable=True)
    voltage_output = Column(String, nullable=True)
    status = Column(SmallInteger, default=0)
    created_by = Column(BigInteger, default=0)
    updated_by = Column(BigInteger, default=0)
    created_at = Column(TIMESTAMP(timezone=True), nullable=True)
    updated_at = Column(TIMESTAMP(timezone=True), nullable=True)
    deleted_at = Column(TIMESTAMP(timezone=True), nullable=True)


def create_inverter(db: Session, control_box_id: int=0, reference: str=None, capacity: str=None, voltage_input: str=None, voltage_output: str=None, status: int=0, created_by: int=0, updated_by: int=0):
    inverter = Inverter(control_box_id=control_box_id, reference=reference, capacity=capacity, voltage_input=voltage_input, voltage_output=voltage_output, status=status, created_by=created_by, updated_by=updated_by, created_at=get_laravel_datetime(), updated_at=get_laravel_datetime())
    db.add(inverter)
    db.commit()
    db.refresh(inverter)
    return inverter

def update_inverter(db: Session, id: int=0, values: Dict={}):
    values['updated_at'] = get_laravel_datetime()
    db.query(Inverter).filter_by(id=id).update(values)
    db.commit()
    return True

def delete_inverter(db: Session, id: int=0):
    values = {
        'deleted_at': get_laravel_datetime(),
    }
    db.query(Inverter).filter_by(id=id).update(values)
    db.commit()
    return True

def get_all_inverters(db: Session):
    return db.query(Inverter).filter(Inverter.deleted_at == None)

def get_all_inverters_by_control_box_id(db: Session, control_box_id: int=0):
    return db.query(Inverter).filter(and_(Inverter.control_box_id == control_box_id, Inverter.deleted_at == None))

def get_inverter_by_id(db: Session, id: int=0):
    return db.query(Inverter).filter_by(id=id).first()
    
def count_inverters(db: Session):
    return db.query(Inverter).filter(Inverter.deleted_at == None).count()
    
def count_inverters_by_control_box_id(db: Session, control_box_id: int=0):
    return db.query(Inverter).filter(and_(Inverter.control_box_id == control_box_id, Inverter.deleted_at == None)).count()
