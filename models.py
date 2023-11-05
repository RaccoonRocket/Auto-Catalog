from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine, MetaData, Table
from config import db_data

Base = declarative_base()

engine = create_engine(db_data)
engine.connect()

metadata = MetaData()
metadata.reflect(bind=engine, schema='car_catalog')


class BrandCountry(Base):
    __table__ = Table('car_catalog.brand_country', metadata, autoload_with=engine)


class CarBrand(Base):
    __table__ = Table('car_catalog.carbrand', metadata, autoload_with=engine)


class ManufacturerCountry(Base):
    __table__ = Table('car_catalog.manufacturer_countries', metadata, autoload_with=engine)


class CarSpecification(Base):
    __table__ = Table('car_catalog.carspecifications', metadata, autoload_with=engine)


class Model(Base):
    __table__ = Table('car_catalog.models', metadata, autoload_with=engine)


class Dealership(Base):
    __table__ = Table('car_catalog.dealerships', metadata, autoload_with=engine)


class Category(Base):
    __table__ = Table('car_catalog.categories', metadata, autoload_with=engine)


class Price(Base):
    __table__ = Table('car_catalog.prices', metadata, autoload_with=engine)


class Description(Base):
    __table__ = Table('car_catalog.description', metadata, autoload_with=engine)


class Image(Base):
    __table__ = Table('car_catalog.images', metadata, autoload_with=engine)


class ModelCategory(Base):
    __table__ = Table('car_catalog.modelcategories', metadata, autoload_with=engine)


class ModelDealership(Base):
    __table__ = Table('car_catalog.modeldealerships', metadata, autoload_with=engine)


class Review(Base):
    __table__ = Table('car_catalog.reviews', metadata, autoload_with=engine)
