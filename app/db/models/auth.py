import datetime as dt
from datetime import datetime, timedelta

from sqlalchemy import Boolean, Column, Date, Enum, String, Integer, DateTime

from app.db import WithTimeStamp


def default_token_expiry() -> datetime:
    return datetime.now(dt.UTC) + timedelta(days=1)


class User(WithTimeStamp):
    __tablename__ = "users"

    email: Column = Column(String(255), unique=True, nullable=False)
    name: Column = Column(String(255), nullable=False)
    gender: Column = Column(Enum("male", "female", name="gender_enum"), default="male")
    date_of_birth: Column = Column(Date, nullable=True)
    phone: Column = Column(String(20), nullable=True)
    address: Column = Column(String(255), nullable=True)
    is_active: Column = Column(Boolean, default=True)

    def __repr__(self):
        return f"<User(name='{self.name}', email='{self.email}')>"


class Token(WithTimeStamp):
    __tablename__ = "tokens"

    access_token: Column = Column(String(255), nullable=False, unique=True)
    user_id: Column = Column(Integer, nullable=False)
    expires_in: Column = Column(DateTime, default=default_token_expiry)
