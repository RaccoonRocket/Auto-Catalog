from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import sessionmaker
from config import db_data
from models import (BrandCountry, CarBrand, ManufacturerCountry, CarSpecification, Model, Dealership,
                    Category, Price, Description, Image, ModelCategory, ModelDealership, Review)
from sqlalchemy import create_engine, MetaData

engine = create_engine(db_data)
engine.connect()

SessionLocal = sessionmaker(autoflush=False, bind=engine)
db = SessionLocal()

# models = db.query(Model).all()
#
# for model in models:
#     print(model.modelid, model.name, model.car_brand_id)

# metadata = MetaData()
# metadata.reflect(bind=engine, schema='car_catalog')
#
# i = 0
# # Print information about the tables and columns in the database
# for table in metadata.tables.values():
#     print("Table Name:", table.name)
#     i += 1
#     for column in table.c:
#         print("Column Name:", column.name)
# print("Total table = ", i)


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

