from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_session
from app.db.models.auth import User
from app.schemas.users.user import UserSchema

router = APIRouter()


@router.get("/", response_model=list[UserSchema])
async def get_users(session: AsyncSession = Depends(get_session)):
    query = select(User)
    result = await session.execute(query)
    users = result.scalars().all()
    return users
