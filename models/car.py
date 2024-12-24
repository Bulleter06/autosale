from sqlalchemy import Column, Integer, String, Float

from modules.database import Base


class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)

    price = Column(Float)
    currency = Column(String)

    year = Column(Integer)

    chassis_type = Column(String)
    engine_volume = Column(Float)

    color = Column(Integer)

