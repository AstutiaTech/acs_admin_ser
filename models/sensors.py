from email.policy import default
from typing import Dict
from sqlalchemy import Column, Integer, String, DateTime, BigInteger, DECIMAL, Float, TIMESTAMP, SmallInteger, Text
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import and_, or_
from sqlalchemy.sql.schema import ForeignKey
from database.db import Base, get_laravel_datetime
import decimal


class Sensor(Base):

    __tablename__ = "sensors"
     
    id = Column(BigInteger, primary_key=True, index=True)
    control_box_id = Column(BigInteger, default=0)
    reference = Column(String, nullable=True)
    sensor_type = Column(Integer, default=0)
    voltage_input = Column(String, nullable=True)
    voltage_output = Column(String, nullable=True)
    status = Column(SmallInteger, default=0)
    created_at = Column(TIMESTAMP(timezone=True), nullable=True)
    updated_at = Column(TIMESTAMP(timezone=True), nullable=True)
    deleted_at = Column(TIMESTAMP(timezone=True), nullable=True)


def create_sensor(db: Session, control_box_id: int=0, reference: str=None, sensor_type: int=0, voltage_input: str=None, voltage_output: str=None, status: int=0):
    sensor = Sensor(control_box_id=control_box_id, reference=reference, sensor_type=sensor_type, voltage_input=voltage_input, voltage_output=voltage_output, status=status, created_at=get_laravel_datetime(), updated_at=get_laravel_datetime())
    db.add(sensor)
    db.commit()
    db.refresh(sensor)
    return sensor

def update_sensor(db: Session, id: int=0, values: Dict={}):
    values['updated_at'] = get_laravel_datetime()
    db.query(Sensor).filter_by(id=id).update(values)
    db.commit()
    return True

def delete_sensor(db: Session, id: int=0):
    values = {
        'deleted_at': get_laravel_datetime(),
    }
    db.query(Sensor).filter_by(id=id).update(values)
    db.commit()
    return True

def get_all_sensors(db: Session):
    return db.query(Sensor).filter(Sensor.deleted_at == None)

def get_all_sensors_by_control_box_id(db: Session, control_box_id: int=0):
    return db.query(Sensor).filter(and_(Sensor.control_box_id == control_box_id, Sensor.deleted_at == None))

def get_sensor_by_id(db: Session, id: int=0):
    return db.query(Sensor).filter_by(id=id).first()
    
def count_sensors(db: Session):
    return db.query(Sensor).filter(Sensor.deleted_at == None).count()
    
def count_sensors_by_control_box_id(db: Session, control_box_id: int=0):
    return db.query(Sensor).filter(and_(Sensor.control_box_id == control_box_id, Sensor.deleted_at == None)).count()
