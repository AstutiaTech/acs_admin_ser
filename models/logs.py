from email.policy import default
from typing import Dict
from sqlalchemy import Column, Integer, String, DateTime, BigInteger, DECIMAL, Float, TIMESTAMP, SmallInteger, Text, desc
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import and_, or_
from sqlalchemy.sql.schema import ForeignKey
from database.db import Base, get_laravel_datetime
import decimal


class Log(Base):

    __tablename__ = "logs"
     
    id = Column(BigInteger, primary_key=True, index=True)
    asset_id = Column(BigInteger, default=0)
    control_box_id = Column(BigInteger, default=0)
    battery_id = Column(BigInteger, default=0)
    inverter_id = Column(BigInteger, default=0)
    sensor_id = Column(BigInteger, default=0)
    port_id = Column(BigInteger, default=0)
    data = Column(String, nullable=True)
    status = Column(SmallInteger, default=0)
    created_at = Column(TIMESTAMP(timezone=True), nullable=True)
    updated_at = Column(TIMESTAMP(timezone=True), nullable=True)
    deleted_at = Column(TIMESTAMP(timezone=True), nullable=True)


def create_log(db: Session, asset_id: int=0, control_box_id: int=0, battery_id: int=0, inverter_id: int=0, sensor_id: int=0, port_id: int=0, data: str=None, status: int=0):
    log = Log(asset_id=asset_id, control_box_id=control_box_id, battery_id=battery_id, inverter_id=inverter_id, sensor_id=sensor_id, port_id=port_id, data=data, status=status, created_at=get_laravel_datetime(), updated_at=get_laravel_datetime())
    db.add(log)
    db.commit()
    db.refresh(log)
    return log

def update_log(db: Session, id: int=0, values: Dict={}):
    values['updated_at'] = get_laravel_datetime()
    db.query(Log).filter_by(id=id).update(values)
    db.commit()
    return True

def get_all_logs(db: Session):
    return db.query(Log).filter(Log.deleted_at == None).order_by(desc(Log.created_at))

def get_all_logs_by_asset_id(db: Session, asset_id: int=0):
    return db.query(Log).filter(and_(Log.asset_id == asset_id, Log.deleted_at == None)).order_by(desc(Log.created_at))

def get_all_logs_by_control_box_id(db: Session, control_box_id: int=0):
    return db.query(Log).filter(and_(Log.control_box_id == control_box_id, Log.deleted_at == None)).order_by(desc(Log.created_at))

def get_all_logs_by_battery_id(db: Session, battery_id: int=0):
    return db.query(Log).filter(and_(Log.battery_id == battery_id, Log.deleted_at == None)).order_by(desc(Log.created_at))

def get_all_logs_by_inverter_id(db: Session, inverter_id: int=0):
    return db.query(Log).filter(and_(Log.inverter_id == inverter_id, Log.deleted_at == None)).order_by(desc(Log.created_at))

def get_all_logs_by_sensor_id(db: Session, sensor_id: int=0):
    return db.query(Log).filter(and_(Log.sensor_id == sensor_id, Log.deleted_at == None)).order_by(desc(Log.created_at))

def get_all_logs_by_port_id(db: Session, port_id: int=0):
    return db.query(Log).filter(and_(Log.port_id == port_id, Log.deleted_at == None)).order_by(desc(Log.created_at))

def get_log_by_id(db: Session, id: int=0):
    return db.query(Log).filter_by(id=id).first()
    
def count_logs(db: Session):
    return db.query(Log).filter(Log.deleted_at == None).count()
    
def count_logs_by_asset_id(db: Session, asset_id: int=0):
    return db.query(Log).filter(and_(Log.asset_id == asset_id, Log.deleted_at == None)).count()

def count_logs_by_control_box_id(db: Session, control_box_id: int=0):
    return db.query(Log).filter(and_(Log.control_box_id == control_box_id, Log.deleted_at == None)).count()

def count_logs_by_battery_id(db: Session, battery_id: int=0):
    return db.query(Log).filter(and_(Log.battery_id == battery_id, Log.deleted_at == None)).count()

def count_logs_by_inverter_id(db: Session, inverter_id: int=0):
    return db.query(Log).filter(and_(Log.inverter_id == inverter_id, Log.deleted_at == None)).count()

def count_logs_by_sensor_id(db: Session, sensor_id: int=0):
    return db.query(Log).filter(and_(Log.sensor_id == sensor_id, Log.deleted_at == None)).count()

def count_logs_by_port_id(db: Session, port_id: int=0):
    return db.query(Log).filter(and_(Log.port_id == port_id, Log.deleted_at == None)).count()
