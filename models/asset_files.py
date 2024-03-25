from email.policy import default
from typing import Dict
from sqlalchemy import Column, Integer, String, DateTime, BigInteger, DECIMAL, Float, TIMESTAMP, SmallInteger, Text
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import and_, or_
from sqlalchemy.sql.schema import ForeignKey
from database.db import Base, get_laravel_datetime
import decimal


class Asset_File(Base):

    __tablename__ = "asset_files"
     
    id = Column(BigInteger, primary_key=True, index=True)
    asset_id = Column(BigInteger, default=0)
    file_type = Column(Integer, default=0)
    file_path = Column(Text, nullable=True)
    file_url = Column(Text, nullable=True)
    status = Column(SmallInteger, default=0)
    created_at = Column(TIMESTAMP(timezone=True), nullable=True)
    updated_at = Column(TIMESTAMP(timezone=True), nullable=True)
    deleted_at = Column(TIMESTAMP(timezone=True), nullable=True)


def create_asset_file(db: Session, asset_id: int=0, file_type: int=0, file_path: str=None, file_url: str=None, status: int=0):
    asset_file = Asset_File(asset_id=asset_id, file_type=file_type, file_path=file_path, file_url=file_url,status=status, created_at=get_laravel_datetime(), updated_at=get_laravel_datetime())
    db.add(asset_file)
    db.commit()
    db.refresh(asset_file)
    return asset_file

def update_asset_file(db: Session, id: int=0, values: Dict={}):
    values['updated_at'] = get_laravel_datetime()
    db.query(Asset_File).filter_by(id=id).update(values)
    db.commit()
    return True

def get_all_asset_files(db: Session):
    return db.query(Asset_File).filter(Asset_File.deleted_at == None).all()

def get_all_asset_files_by_asset_id(db: Session, asset_id: int=0):
    return db.query(Asset_File).filter(and_(Asset_File.deleted_at == None, Asset_File.asset_id == asset_id)).all()

def get_asset_file_by_id(db: Session, id: int=0):
    return db.query(Asset_File).filter_by(id=id).first()
    
def count_asset_files(db: Session):
    return db.query(Asset_File).filter(Asset_File.deleted_at == None).count()

def count_asset_files_by_asset_id(db: Session, asset_id: int=0):
    return db.query(Asset_File).filter(and_(Asset_File.deleted_at == None, Asset_File.asset_id == asset_id)).count()
