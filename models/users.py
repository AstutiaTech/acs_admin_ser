from email.policy import default
from typing import Dict
from sqlalchemy import Column, Integer, String, DateTime, BigInteger, DECIMAL, Float, TIMESTAMP, SmallInteger, Text
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import and_, or_
from sqlalchemy.sql.schema import ForeignKey
from database.db import Base, get_laravel_datetime
import decimal


class User(Base):

    __tablename__ = "users"
     
    id = Column(BigInteger, primary_key=True, index=True)
    owner_id = Column(BigInteger, default=0)
    username = Column(String, nullable=True)
    email = Column(String, nullable=True)
    password = Column(String, nullable=True)
    pin = Column(String, nullable=True)
    role = Column(SmallInteger, default=0)
    status = Column(SmallInteger, default=0)
    created_at = Column(TIMESTAMP(timezone=True), nullable=True)
    updated_at = Column(TIMESTAMP(timezone=True), nullable=True)
    deleted_at = Column(TIMESTAMP(timezone=True), nullable=True)


def create_user(db: Session, owner_id: int=0, username: str=None, email: str=None, phone_number: str=None, password: str=None, pin: str=None, role: int=0, status: int=0):
    user = User(owner_id=owner_id, username=username, email=email, phone_number=phone_number, password=password, pin=pin, role=role, status=status, created_at=get_laravel_datetime(), updated_at=get_laravel_datetime())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def update_user(db: Session, id: int=0, values: Dict={}):
    values['updated_at'] = get_laravel_datetime()
    db.query(User).filter_by(id=id).update(values)
    db.commit()
    return True

def get_all_users(db: Session):
    return db.query(User).all()

def get_user_by_id(db: Session, id: int=0):
    return db.query(User).filter_by(id=id).first()
    
def get_user_by_email(db: Session, email: str=None):
    return db.query(User).filter_by(email=email).first()
    
def get_user_by_username(db: Session, username: str=None):
    return db.query(User).filter_by(username=username).first()
    
def user_login(db: Session, field: str=None):
    return db.query(User).filter(and_(or_(User.email == field, User.username == field), User.status == 1, User.deleted_at == None)).first()

def count_users(db: Session):
    return db.query(User).count()

def count_user_by_email(db: Session, email: str=None):
    return db.query(User).filter_by(email=email).count()
    
def count_user_by_username(db: Session, username: str=None):
    return db.query(User).filter_by(username=username).count()
    