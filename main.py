from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from sqlalchemy import create_engine
import psycopg2
from config import db_data

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

engine = create_engine(db_data)
engine.connect()

print(engine)
