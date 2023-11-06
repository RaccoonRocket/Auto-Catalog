from fastapi import FastAPI, Depends, Body
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session, session
from database import *
from fastapi.responses import JSONResponse, FileResponse

# app
app = FastAPI()

# connecting static files
app.mount("/static", StaticFiles(directory="static"), name="static")


# defining the dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def main():
    return FileResponse("templates/index.html")


@app.get("/api/models")
def get_models(db: Session = Depends(get_db)):
    res = db.query(Model.modelid, CarBrand.car_brand_name, Model.name).join(CarBrand, Model.car_brand_id == CarBrand.car_brand_id).all()
    processed_res = [(item[0], item[1], item[2]) for item in res1]
    return processed_res
    # return db.query(Model).all()


# SessionLocal = sessionmaker(autoflush=False, bind=engine)
db = SessionLocal()

res1 = db.query(Model.modelid, CarBrand.car_brand_name, Model.name).join(CarBrand, Model.car_brand_id == CarBrand.car_brand_id).all()
processed_res1 = [{item[0], item[1], item[2]} for item in res1]
res2 = db.query(Model).all()

for result in res1:
    print(result)

# # Print information about the tables and columns in the database
# for table in metadata.tables.values():
#     print("Table Name:", table.name)
#     for column in table.c:
#         print("Column Name:", column.name)
