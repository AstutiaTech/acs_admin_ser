from email.policy import default
from typing import Dict
from sqlalchemy import Column, Integer, String, DateTime, BigInteger, DECIMAL, Float, TIMESTAMP, SmallInteger, Text
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import and_, or_
from sqlalchemy.sql.schema import ForeignKey
from database.db import Base, get_laravel_datetime
import decimal


class Port(Base):

    __tablename__ = "ports"
     
    id = Column(BigInteger, primary_key=True, index=True)
    room_id = Column(BigInteger, default=0)
    control_box_id = Column(BigInteger, default=0)
    port_type_id = Column(BigInteger, default=0)
    reference = Column(String, nullable=True)
    appliance_name = Column(String, nullable=True)
    room_name = Column(String, nullable=True)
    power_rating = Column(String, nullable=True)
    current_drawn = Column(String, nullable=True)
    priority_status = Column(Integer, default=0)
    status = Column(SmallInteger, default=0)
    created_by = Column(BigInteger, default=0)
    updated_by = Column(BigInteger, default=0)
    created_at = Column(TIMESTAMP(timezone=True), nullable=True)
    updated_at = Column(TIMESTAMP(timezone=True), nullable=True)
    deleted_at = Column(TIMESTAMP(timezone=True), nullable=True)


def create_port(db: Session, room_id: int=0, control_box_id: int=0, port_type_id: int=0, reference: str=None, appliance_name: str=None, room_name: str=None, power_rating: str=None, current_drawn: str=None, priority_status: int=0, status: int=0, created_by: int=0, updated_by: int=0):
    port = Port(room_id=room_id, control_box_id=control_box_id, port_type_id=port_type_id, reference=reference, appliance_name=appliance_name, room_name=room_name, power_rating=power_rating, current_drawn=current_drawn, priority_status=priority_status, status=status, created_by=created_by, updated_by=updated_by, created_at=get_laravel_datetime(), updated_at=get_laravel_datetime())
    db.add(port)
    db.commit()
    db.refresh(port)
    return port

def update_port(db: Session, id: int=0, values: Dict={}):
    values['updated_at'] = get_laravel_datetime()
    db.query(Port).filter_by(id=id).update(values)
    db.commit()
    return True

def delete_port(db: Session, id: int=0):
    values = {
        'deleted_at': get_laravel_datetime(),
    }
    db.query(Port).filter_by(id=id).update(values)
    db.commit()
    return True

def get_all_ports(db: Session):
    return db.query(Port).filter(Port.deleted_at == None)

def get_all_ports_by_room_id(db: Session, room_id: int=0):
    return db.query(Port).filter(and_(Port.room_id == room_id, Port.deleted_at == None))

def get_all_ports_by_control_box_id(db: Session, control_box_id: int=0):
    return db.query(Port).filter(and_(Port.control_box_id == control_box_id, Port.deleted_at == None))

def get_all_ports_by_port_type_id(db: Session, port_type_id: int=0):
    return db.query(Port).filter(and_(Port.port_type_id == port_type_id, Port.deleted_at == None))

def get_all_ports_by_room_id_and_port_type_id(db: Session, room_id: int=0, port_type_id: int=0):
    return db.query(Port).filter(and_(Port.room_id == room_id, Port.port_type_id == port_type_id, Port.deleted_at == None))

def get_all_ports_by_control_box_id_and_port_type_id(db: Session, control_box_id: int=0, port_type_id: int=0):
    return db.query(Port).filter(and_(Port.control_box_id == control_box_id, Port.port_type_id == port_type_id, Port.deleted_at == None))

def get_port_by_id(db: Session, id: int=0):
    return db.query(Port).filter_by(id=id).first()
    
def count_ports(db: Session):
    return db.query(Port).filter(Port.deleted_at == None).count()
    
def count_ports_by_room_id(db: Session, room_id: int=0):
    return db.query(Port).filter(and_(Port.room_id == room_id, Port.deleted_at == None)).count()

def count_ports_by_control_box_id(db: Session, control_box_id: int=0):
    return db.query(Port).filter(and_(Port.control_box_id == control_box_id, Port.deleted_at == None)).count()

def count_ports_by_port_type_id(db: Session, port_type_id: int=0):
    return db.query(Port).filter(and_(Port.port_type_id == port_type_id, Port.deleted_at == None)).count()
