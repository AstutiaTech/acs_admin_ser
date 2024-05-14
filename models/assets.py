from email.policy import default
from typing import Dict
from sqlalchemy import Column, Integer, String, DateTime, BigInteger, DECIMAL, Float, TIMESTAMP, SmallInteger, Text, desc
from sqlalchemy.orm import Session, joinedload, relationship
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import and_, or_
from sqlalchemy.sql.schema import ForeignKey
from database.db import Base, get_laravel_datetime
import decimal
from models.asset_files import Asset_File


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

    asset_files = relationship("Asset_File", back_populates="asset")


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

def delete_asset(db: Session, id: int=0):
    values = {
        'deleted_at': get_laravel_datetime(),
    }
    db.query(Asset).filter_by(id=id).update(values)
    db.commit()
    return True

def get_all_assets(db: Session):
    return db.query(Asset).filter(Asset.deleted_at == None).all()

def get_all_assets_paginated(db: Session):
    return db.query(Asset).filter(Asset.deleted_at == None).order_by(desc(Asset.created_at))

def get_all_assets_paginated_with_files(db: Session):
    return db.query(Asset).join(Asset_File, Asset.id == Asset_File.asset_id).filter(and_(Asset.deleted_at == None, Asset_File.deleted_at == None)).options(joinedload(Asset.asset_files)).order_by(desc(Asset.created_at))

def get_assets_by_owner_id(db: Session, owner_id: int=0):
    return db.query(Asset).filter(and_(Asset.owner_id == owner_id, Asset.deleted_at == None)).order_by(desc(Asset.created_at))

def get_assets_by_owner_id_with_files(db: Session, owner_id: int=0):
    return db.query(Asset).join(Asset_File, Asset.id == Asset_File.asset_id).filter(and_(Asset.owner_id == owner_id, Asset.deleted_at == None, Asset_File.deleted_at == None)).options(joinedload(Asset.asset_files)).order_by(desc(Asset.created_at))

def get_asset_by_id(db: Session, id: int=0):
    return db.query(Asset).filter_by(id=id).first()

def get_asset_by_id_with_files(db: Session, id: int=0):
    return db.query(Asset).join(Asset_File, Asset.id == Asset_File.asset_id).filter(and_(Asset.id == id, Asset_File.deleted_at == None)).options(joinedload(Asset.asset_files)).first()
    
def count_assets(db: Session):
    return db.query(Asset).filter(Asset.deleted_at == None).count()
