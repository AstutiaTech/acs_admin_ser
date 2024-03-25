from email.policy import default
from typing import Dict
from sqlalchemy import Column, Integer, String, DateTime, BigInteger, DECIMAL, Float, TIMESTAMP, SmallInteger, Text
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import and_, or_
from sqlalchemy.sql.schema import ForeignKey
from database.db import Base, get_laravel_datetime
import decimal


class Admin(Base):

    __tablename__ = "admins"
     
    id = Column(BigInteger, primary_key=True, index=True)
    username = Column(String, nullable=True)
    email = Column(String, nullable=True)
    password = Column(String, nullable=True)
    role = Column(Integer, default=0)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    status = Column(SmallInteger, default=0)
    created_at = Column(TIMESTAMP(timezone=True), nullable=True)
    updated_at = Column(TIMESTAMP(timezone=True), nullable=True)
    deleted_at = Column(TIMESTAMP(timezone=True), nullable=True)


def create_admin(db: Session, username: str=None, email: str=None, password: str=None, role: int=0, first_name: str=None, last_name: str=None, status: int=0):
    admin = Admin(username=username, email=email, password=password, role=role, first_name=first_name, last_name=last_name, status=status, created_at=get_laravel_datetime(), updated_at=get_laravel_datetime())
    db.add(admin)
    db.commit()
    db.refresh(admin)
    return admin

def update_admin(db: Session, id: int=0, values: Dict={}):
    values['updated_at'] = get_laravel_datetime()
    db.query(Admin).filter_by(id=id).update(values)
    db.commit()
    return True

def get_all_admin(db: Session):
    return db.query(Admin).filter(Admin.deleted_at == None).all()

def get_admin_by_id(db: Session, id: int=0):
    return db.query(Admin).filter_by(id=id).first()
    
def get_admin_by_email(db: Session, email: str=None):
    return db.query(Admin).filter_by(email=email).first()
    
def get_admin_by_username(db: Session, username: str=None):
    return db.query(Admin).filter_by(username=username).first()
    
def admin_login(db: Session, field: str=None):
    return db.query(Admin).filter(and_(or_(Admin.username == field, Admin.email == field), Admin.status == 1, Admin.deleted_at == None)).first()

def count_admins(db: Session):
    return db.query(Admin).filter(Admin.deleted_at == None).count()
