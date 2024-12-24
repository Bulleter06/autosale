import datetime
from enum import Enum, IntEnum

from pydantic import BaseModel


class CurrencyEnum(Enum):
    usd = 'USD'
    uah = 'UAH'


class ChassisEnum(Enum):
    coupe = 'coupe'
    sedan = 'sedan'


class ColorEnum(IntEnum):
    black = 0
    white = 1
    pink = 2
    silver = 3


class Car(BaseModel):
    name: str
    description: str
    price: float
    currency: CurrencyEnum
    year: int
    chassis_type: ChassisEnum
    engine_volume: float
    color: ColorEnum


class CarRead(Car):
    id: int
