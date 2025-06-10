from sqlalchemy import Column, String, Enum, Date, Boolean

from app.db import WithTimeStamp


class User(WithTimeStamp):
    __tablename__ = "users"

    email = Column(String(255), unique=True, nullable=False)
    name = Column(String(255), nullable=False)
    gender = Column(Enum("male", "female", name="gender_enum"), default="male")
    date_of_birth = Column(Date, nullable=False)
    phone = Column(String(20), nullable=True)
    address = Column(String(255), nullable=True)
    is_active = Column(Boolean, default=True)

    def __repr__(self):
        return f"<User(name='{self.name}', email='{self.email}')>"
