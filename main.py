from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import sessionmaker
from config import db_data
from models import Dealership
from sqlalchemy import create_engine

engine = create_engine(db_data)
engine.connect()

SessionLocal = sessionmaker(autoflush=False, bind=engine)
db = SessionLocal()

models = db.query(Dealership).all()

for model in models:
    print(model.dealershipid, model.name, model.address, model.phone, model.city)


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

