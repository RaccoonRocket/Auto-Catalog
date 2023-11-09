from fastapi import FastAPI, Depends, Body
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
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


@app.get("/api/models/{nameCategory}/{minPrice}/{maxPrice}")
def selector_models(nameCategory, minPrice, maxPrice, db: Session = Depends(get_db)):
    if nameCategory=="Все":
        models = (db.query(Model.modelid, Image.url, Model.name, CarBrand.car_brand_name, Category.name, Price.price).
                  join(Image, Model.modelid == Image.model_id).
                  join(CarBrand, Model.car_brand_id == CarBrand.car_brand_id).
                  join(ModelCategory, Model.modelid == ModelCategory.modelid).
                  join(Category, ModelCategory.categoryid == Category.categoryid).
                  join(Price, Model.modelid == Price.model_id).
                  filter(Price.price >= minPrice).
                  filter(Price.price <= maxPrice).all())
    else:
        models = (db.query(Model.modelid, Image.url, Model.name, CarBrand.car_brand_name, Category.name, Price.price).
                  join(Image, Model.modelid == Image.model_id).
                  join(CarBrand, Model.car_brand_id == CarBrand.car_brand_id).
                  join(ModelCategory, Model.modelid == ModelCategory.modelid).
                  join(Category, ModelCategory.categoryid == Category.categoryid).
                  join(Price, Model.modelid == Price.model_id).
                  filter(Category.name == nameCategory).
                  filter(Price.price >= minPrice).
                  filter(Price.price <= maxPrice).all())
    processed_models = [(item[0], item[1], item[2], item[3], item[4], item[5]) for item in models]
    return processed_models


# @app.get("/model")
# def view_model():
#     return FileResponse("templates/about_model.html")
#
#
# @app.get("/brand/{brandName}")
# def view_brand():
#     return FileResponse("templates/about_brand.html")


@app.get("/api/models")
def get_all_models(db: Session = Depends(get_db)):
    models = (db.query(Model.modelid, Image.url, Model.name, CarBrand.car_brand_name, Category.name, Price.price).
              join(Image, Model.modelid == Image.model_id).
              join(CarBrand, Model.car_brand_id == CarBrand.car_brand_id).
              join(ModelCategory, Model.modelid == ModelCategory.modelid).
              join(Category, ModelCategory.categoryid == Category.categoryid).
              join(Price, Model.modelid == Price.model_id).all())
    processed_models = [(item[0], item[1], item[2], item[3], item[4], item[5]) for item in models]
    return processed_models


# @app.get("/api/models/{modelName}")
# def get_model(modelName, db: Session = Depends(get_db)):
#     # getting model by id
#     model = (db.query(Model.name).filter(Model.name == modelName).all())
#     # if not found, sending 404 & error message
#     if model==None:
#         return JSONResponse(status_code=404, content={"message": "Модель не найден"})
#     # if found, sending it
#     return model
#
#
# @app.get("/api/brands/{brandName}")
# def get_brand(brandName, db: Session = Depends(get_db)):
#     # getting brand by id
#     brand = (db.query(CarBrand.car_brand_name, ManufacturerCountry.name).
#              join(BrandCountry, CarBrand.car_brand_id == BrandCountry.car_brand_id).
#              join(ManufacturerCountry, BrandCountry.manufacturer_country_id == ManufacturerCountry.manufacturerid).
#              filter(CarBrand.car_brand_name == brandName).all())
#     # if not found, sending 404 & error message
#     if brand==None:
#         return JSONResponse(status_code=404, content={"message": "Бренд не найден"})
#     # if found, sending it
#     return brand


# SessionLocal = sessionmaker(autoflush=False, bind=engine)
# db = SessionLocal()
#
# res1 = db.query(Model.modelid, CarBrand.car_brand_name, Model.name).join(CarBrand, Model.car_brand_id == CarBrand.car_brand_id).all()
# processed_res1 = [{item[0], item[1], item[2]} for item in res1]
# res2 = db.query(Model).all()
# models = (db.query(Model.modelid, Image.url, Model.name, CarBrand.car_brand_name, Category.name, Price.price).
#               join(Image, Model.modelid == Image.model_id).
#               join(CarBrand, Model.car_brand_id == CarBrand.car_brand_id).
#               join(ModelCategory, Model.modelid == ModelCategory.modelid).
#               join(Category, ModelCategory.categoryid == Category.categoryid).
#               join(Price, Model.modelid == Price.model_id).all())
# processed_models = [(item[0], item[1], item[2], item[3], item[4], item[5]) for item in models]
# for result in models:
#     print(result)

# brand = (db.query(CarBrand.car_brand_name, ManufacturerCountry.name).
#          join(BrandCountry, CarBrand.car_brand_id == BrandCountry.car_brand_id).
#          join(ManufacturerCountry, BrandCountry.manufacturer_country_id == ManufacturerCountry.manufacturerid).
#          filter(CarBrand.car_brand_id == 21).all())
#
# processed_brand = [(item[0], item[1]) for item in brand]
# for result in brand:
#      print(result)

# model = db.query(Model.name).all()
# print(model)
#
# # # Print information about the tables and columns in the database
# for table in metadata.tables.values():
#     print("Table Name:", table.name)
#     for column in table.c:
#         print("Column Name:", column.name)
