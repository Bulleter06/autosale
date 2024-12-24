from fastapi import FastAPI

from routers.car import car_router
from modules.database import sessionmanager
app = FastAPI()
app.include_router(car_router)
