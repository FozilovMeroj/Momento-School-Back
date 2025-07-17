from sqlalchemy import Boolean, Column, Date, Enum, String

from app.db import WithTimeStamp


class User(WithTimeStamp):
    __tablename__ = "users"

    email: Column = Column(String(255), unique=True, nullable=False)
    name: Column = Column(String(255), nullable=False)
    gender: Column = Column(Enum("male", "female", name="gender_enum"), default="male")
    date_of_birth: Column = Column(Date, nullable=False)
    phone: Column = Column(String(20), nullable=True)
    address: Column = Column(String(255), nullable=True)
    is_active: Column = Column(Boolean, default=True)

    def __repr__(self):
        return f"<User(name='{self.name}', email='{self.email}')>"
