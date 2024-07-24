from email.policy import default
from typing import Dict
from sqlalchemy import Column, Integer, String, DateTime, BigInteger, DECIMAL, Float, TIMESTAMP, SmallInteger, Text, desc
from sqlalchemy.orm import Session, relationship
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import and_, or_
from sqlalchemy.sql.schema import ForeignKey
from database.db import Base, get_laravel_datetime
import decimal


class Port_Type(Base):

    __tablename__ = "port_types"
     
    id = Column(BigInteger, primary_key=True, index=True)
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


def create_port_type(db: Session, name: str=None, description: str=None, file_url: str=None, slug: str=None, value_code: str=None, status: int=0, created_by: int=0, updated_by: int=0):
    port_type = Port_Type(name=name, description=description, file_url=file_url, slug=slug, value_code=value_code, status=status, created_by=created_by, updated_by=updated_by, created_at=get_laravel_datetime(), updated_at=get_laravel_datetime())
    db.add(port_type)
    db.commit()
    db.refresh(port_type)
    return port_type

def update_port_type(db: Session, id: int=0, values: Dict={}):
    values['updated_at'] = get_laravel_datetime()
    db.query(Port_Type).filter_by(id=id).update(values)
    db.commit()
    return True

def delete_port_type(db: Session, id: int=0):
    values = {
        'deleted_at': get_laravel_datetime(),
    }
    db.query(Port_Type).filter_by(id=id).update(values)
    db.commit()
    return True

def get_all_port_types(db: Session):
    return db.query(Port_Type).filter(Port_Type.deleted_at == None).order_by(desc(Port_Type.created_at))

def get_port_type_by_id(db: Session, id: int=0):
    return db.query(Port_Type).filter_by(id=id).first()
    
def count_port_types(db: Session):
    return db.query(Port_Type).filter(Port_Type.deleted_at == None).count()
