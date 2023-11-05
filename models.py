from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine, MetaData, Table
from config import db_data

Base = declarative_base()

engine = create_engine(db_data)
engine.connect()

metadata = MetaData()
metadata.reflect(bind=engine, schema='car_catalog')


class Dealership(Base):
    __table__ = Table('car_catalog.dealerships', metadata, autoload_with=engine)
