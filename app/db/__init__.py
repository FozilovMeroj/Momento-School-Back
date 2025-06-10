from typing import Any, AsyncGenerator

from sqlalchemy import Column, DateTime, Integer, func
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from .. import config as db_config

engine = create_async_engine(db_config.DATABASE_URL)
new_session = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


class WithTimeStamp(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())


async def get_session() -> AsyncGenerator[AsyncSession, Any]:
    async with new_session() as session:
        yield session
