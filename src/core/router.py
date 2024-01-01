from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session

from core.models import Articles

router = APIRouter(
    prefix='/core',
    tags=['Core']
)


@router.get("/")
async def get_article(session: AsyncSession = Depends(get_async_session)):
    query = select(Articles)
    result = await session.execute(query)

    return result.all()
