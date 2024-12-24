import traceback
from typing import List

from fastapi import APIRouter, Depends, HTTPException

from crud.car import CarCrud
from modules.database import get_db_session
from schemas.car import Car, CarRead

car_router = APIRouter(prefix='/cars')


@car_router.get('/', response_model=List[CarRead])
async def get_cars(session=Depends(get_db_session)):
    return await CarCrud.read_all(session)


@car_router.get('/{car_id}', response_model=CarRead)
async def get_car(car_id: int, session=Depends(get_db_session)):
    result = await CarCrud.read(session, identification=car_id)

    if not result:
        raise HTTPException(status_code=404, detail='Car not found')

    return result


@car_router.post('/create', response_model=None)
async def create_car(car: Car, session=Depends(get_db_session)):
    try:
        return await CarCrud.create(session=session, schema=car)

    except:
        raise HTTPException(status_code=500, detail='Failed to create new car')
