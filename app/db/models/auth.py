import datetime as dt
from datetime import datetime, timedelta

from sqlalchemy import Boolean, Column, Date, Enum, String, Integer, DateTime

from app.db import WithTimeStamp
from app.enums import GenderEnum


def default_token_expiry() -> datetime:
    return datetime.now(dt.UTC) + timedelta(days=1)


class User(WithTimeStamp):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email: Column = Column(String(255), unique=True, nullable=False)
    name: Column = Column(String(255), nullable=False)
    gender: Column = Column(Enum(GenderEnum), default="male")
    date_of_birth: Column = Column(Date, nullable=True)
    phone: Column = Column(String(20), nullable=True)
    address: Column = Column(String(255), nullable=True)
    is_active: Column = Column(Boolean, default=True)


class Token(WithTimeStamp):
    __tablename__ = "tokens"

    id = Column(Integer, primary_key=True)
    access_token: Column = Column(String(255), nullable=False, unique=True)
    user_id: Column = Column(Integer, nullable=False)
    expires_in: Column = Column(DateTime, default=default_token_expiry)
