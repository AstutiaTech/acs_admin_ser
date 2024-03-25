from email.policy import default
from typing import Dict
from sqlalchemy import Column, Integer, String, DateTime, BigInteger, DECIMAL, Float, TIMESTAMP, SmallInteger, Text
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import and_, or_
from sqlalchemy.sql.schema import ForeignKey
from database.db import Base, get_laravel_datetime
import decimal


class Asset(Base):

    __tablename__ = "assets"
     
    id = Column(BigInteger, primary_key=True, index=True)
    owner_id = Column(BigInteger, default=0)
    reference = Column(String, nullable=True)
    asset_type = Column(Integer, default=0)
    name = Column(String, nullable=True)
    description = Column(Text, nullable=True)
    address = Column(String, nullable=True)
    city = Column(String, nullable=True)
    state = Column(String, nullable=True)
    country = Column(String, nullable=True)
    latitude = Column(String, nullable=True)
    longitude = Column(String, nullable=True)
    status = Column(SmallInteger, default=0)
    created_at = Column(TIMESTAMP(timezone=True), nullable=True)
    updated_at = Column(TIMESTAMP(timezone=True), nullable=True)
    deleted_at = Column(TIMESTAMP(timezone=True), nullable=True)


def create_asset(db: Session, owner_id: int=0, reference: str=None, asset_type: int=0, name: str=None, description: str=None, address: str=None, city: str=None, state: str=None, country: str=None, latitude: str=None, longitude: str=None, status: int=0):
    asset = Asset(owner_id=owner_id, reference=reference, asset_type=asset_type, name=name, description=description, address=address, city=city, state=state, country=country, latitude=latitude, longitude=longitude, status=status, created_at=get_laravel_datetime(), updated_at=get_laravel_datetime())
    db.add(asset)
    db.commit()
    db.refresh(asset)
    return asset

def update_asset(db: Session, id: int=0, values: Dict={}):
    values['updated_at'] = get_laravel_datetime()
    db.query(Asset).filter_by(id=id).update(values)
    db.commit()
    return True

def get_all_assets(db: Session):
    return db.query(Asset).filter(Asset.deleted_at == None).all()

def get_asset_by_id(db: Session, id: int=0):
    return db.query(Asset).filter_by(id=id).first()
    
def count_assets(db: Session):
    return db.query(Asset).filter(Asset.deleted_at == None).count()
