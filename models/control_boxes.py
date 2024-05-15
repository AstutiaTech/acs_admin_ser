from email.policy import default
from typing import Dict
from sqlalchemy import Column, Integer, String, DateTime, BigInteger, DECIMAL, Float, TIMESTAMP, SmallInteger, Text
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import and_, or_
from sqlalchemy.sql.schema import ForeignKey
from database.db import Base, get_laravel_datetime
import decimal


class Control_Box(Base):

    __tablename__ = "control_boxes"
     
    id = Column(BigInteger, primary_key=True, index=True)
    asset_id = Column(BigInteger, default=0)
    reference = Column(String, nullable=True)
    private_key = Column(String, nullable=True)
    comms_sim_card_value = Column(String, nullable=True)
    comms_sim_card_number = Column(String, nullable=True)
    comms_wifi_provider = Column(String, nullable=True)
    status = Column(SmallInteger, default=0)
    created_at = Column(TIMESTAMP(timezone=True), nullable=True)
    updated_at = Column(TIMESTAMP(timezone=True), nullable=True)
    deleted_at = Column(TIMESTAMP(timezone=True), nullable=True)


def create_control_box(db: Session, asset_id: int=0, reference: str=None, private_key: str=None, comms_sim_card_value: str=None, comms_sim_card_number: str=None, comms_wifi_provider: str=None, status: int=0):
    cb = Control_Box(asset_id=asset_id, reference=reference, private_key=private_key, comms_sim_card_value=comms_sim_card_value, comms_sim_card_number=comms_sim_card_number, comms_wifi_provider=comms_wifi_provider, status=status, created_at=get_laravel_datetime(), updated_at=get_laravel_datetime())
    db.add(cb)
    db.commit()
    db.refresh(cb)
    return cb

def update_control_box(db: Session, id: int=0, values: Dict={}):
    values['updated_at'] = get_laravel_datetime()
    db.query(Control_Box).filter_by(id=id).update(values)
    db.commit()
    return True

def delete_control_box(db: Session, id: int=0):
    values = {
        'deleted_at': get_laravel_datetime(),
    }
    db.query(Control_Box).filter_by(id=id).update(values)
    db.commit()
    return True

def get_all_control_boxes(db: Session):
    return db.query(Control_Box).filter(Control_Box.deleted_at == None)

def get_all_control_boxes_by_asset_id(db: Session, asset_id: int=0):
    return db.query(Control_Box).filter(and_(Control_Box.asset_id == asset_id, Control_Box.deleted_at == None))

def get_control_box_by_id(db: Session, id: int=0):
    return db.query(Control_Box).filter_by(id=id).first()
    
def count_control_boxes(db: Session):
    return db.query(Control_Box).filter(Control_Box.deleted_at == None).count()
    
def count_control_boxes_by_asset_id(db: Session, asset_id: int=0):
    return db.query(Control_Box).filter(and_(Control_Box.asset_id == asset_id, Control_Box.deleted_at == None)).count()
