from pydantic import BaseModel
from sqlalchemy import select, delete
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm.sync import update


class AbstractCrud:
    model = None

    @classmethod
    async def create(cls, session: AsyncSession, schema: BaseModel):
        new_model = cls.model(**schema.model_dump(mode='json'))
        session.add(new_model)
        try:
            await session.commit()
            await session.refresh(new_model)
            return new_model

        except IntegrityError as e:
            await session.rollback()
            raise e

    @classmethod
    async def read(cls, session: AsyncSession, identification: int):
        result = await session.execute(select(cls.model).where(cls.model.id == identification))
        return result.scalars().first()

    # @classmethod
    # async def read_with_filter(cls, session: AsyncSession, key:str, value:int):
    #     result = await session.execute(select(cls.model).where(cls.model.year > 5))
    #     return result.scalars().first()

    @classmethod
    async def read_all(cls, session: AsyncSession):
        # await session.execute(select(cls.model).offset(value).limit(limit))
        results = await session.execute(select(cls.model))
        return results.scalars().all()

    @classmethod
    async def update(cls, session: AsyncSession, identification, schema):
        updated_model = update(cls.model).where(cls.model == identification).values(**schema.model_dump(mode='json'))
        try:
            await session.execute(updated_model)
            await session.commit()
            return cls.read(session, identification)
        except IntegrityError as e:
            await session.rollback()
            raise e

    @classmethod
    async def delete(cls, session: AsyncSession, identification: int):
        model_to_delete = delete(cls.model).where(cls.model == identification)
        try:
            await session.execute(model_to_delete)
            await session.commit()
            return {'status': 'Model was deleted'}
        except IntegrityError as e:
            await session.rollback()
            raise e
