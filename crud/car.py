from crud.abstract import AbstractCrud
from models.car import Car


class CarCrud(AbstractCrud):
    model = Car