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


@app.get("/api/models")
def get_models(db: Session = Depends(get_db)):
    models = (db.query(Model.modelid, Image.url, Model.name, CarBrand.car_brand_name, Category.name, Price.price).
              join(Image, Model.modelid == Image.model_id).
              join(CarBrand, Model.car_brand_id == CarBrand.car_brand_id).
              join(ModelCategory, Model.modelid == ModelCategory.modelid).
              join(Category, ModelCategory.categoryid == Category.categoryid).
              join(Price, Model.modelid == Price.model_id).
              order_by(Price.price.asc()).all())
    processed_models = [(item[0], item[1], item[2], item[3], item[4], item[5]) for item in models]
    return processed_models


@app.get("/api/models/{brands}/{categories}/{prices}")
def select_models(brands, categories, prices, db: Session = Depends(get_db)):
    brands = brands.split(',')
    categories = categories.split(',')
    prices = prices.split(',')
    print(brands)
    print(categories)
    print(prices)
    if (prices[2] == "asc"):
        models = (db.query(Model.modelid, Image.url, Model.name, CarBrand.car_brand_name, Category.name, Price.price).
                  join(Image, Model.modelid == Image.model_id).
                  join(CarBrand, Model.car_brand_id == CarBrand.car_brand_id).
                  join(ModelCategory, Model.modelid == ModelCategory.modelid).
                  join(Category, ModelCategory.categoryid == Category.categoryid).
                  join(Price, Model.modelid == Price.model_id).
                  filter(CarBrand.car_brand_name.in_(brands)).
                  filter(Category.name.in_(categories)).
                  filter(Price.price >= prices[0]).
                  filter(Price.price <= prices[1]).
                  order_by(Price.price.asc()).all())
    else:
        models = (db.query(Model.modelid, Image.url, Model.name, CarBrand.car_brand_name, Category.name, Price.price).
                  join(Image, Model.modelid == Image.model_id).
                  join(CarBrand, Model.car_brand_id == CarBrand.car_brand_id).
                  join(ModelCategory, Model.modelid == ModelCategory.modelid).
                  join(Category, ModelCategory.categoryid == Category.categoryid).
                  join(Price, Model.modelid == Price.model_id).
                  filter(CarBrand.car_brand_name.in_(brands)).
                  filter(Category.name.in_(categories)).
                  filter(Price.price >= prices[0]).
                  filter(Price.price <= prices[1]).
                  order_by(Price.price.desc()).all())
    processed_models = [(item[0], item[1], item[2], item[3], item[4], item[5]) for item in models]
    return processed_models


# @app.get("/models")
# def get_brand():
#     return FileResponse("templates/about_models.html")
#
#
# @app.get("/brands")
# def get_brand():
#     return FileResponse("templates/about_brands.html")
#
#
# @app.get("/api/models/{modelName}")
# def get_brand_info(modelName, db: Session = Depends(get_db)):
#     model = (db.query(Model.modelid, Image.url, Model.name, CarBrand.car_brand_name, Price.price,
#                        Description.description, Review.title, Review.text, Review.rating, Review.date).
#               join(Image, Model.modelid == Image.model_id).
#               join(CarBrand, Model.car_brand_id == CarBrand.car_brand_id).
#               join(Price, Model.modelid == Price.model_id).
#               join(Description, Model.modelid == Description.description_id).
#               join(Review, Model.modelid == Review.reviewid).all())
#     processed_model = [(item[0], item[1], item[2], item[3], item[4], item[5], item[6],
#                          item[7], item[8], item[9]) for item in model]
#     return processed_model
#
#
# @app.get("/api/brands/{brandName}")
# def get_brand_info(brandName, db: Session = Depends(get_db)):
#     brand = (db.query(ManufacturerCountry.manufacturerid, ManufacturerCountry.name).
#              join(BrandCountry, ManufacturerCountry.manufacturerid == BrandCountry.manufacturer_country_id).
#              join(CarBrand, BrandCountry.car_brand_id == CarBrand.car_brand_id).
#              filter(CarBrand.car_brand_name == brandName).all())
#     processed_brand = [(item[0], item[1]) for item in brand]
#     return processed_brand
#
#
# @app.get("/api/models/{nameCategory}/{minPrice}/{maxPrice}")
# def selector_models(nameCategory, minPrice, maxPrice, db: Session = Depends(get_db)):
#     if nameCategory=="Все":
#         models = (db.query(Model.modelid, Image.url, Model.name, CarBrand.car_brand_name, Category.name, Price.price).
#                   join(Image, Model.modelid == Image.model_id).
#                   join(CarBrand, Model.car_brand_id == CarBrand.car_brand_id).
#                   join(ModelCategory, Model.modelid == ModelCategory.modelid).
#                   join(Category, ModelCategory.categoryid == Category.categoryid).
#                   join(Price, Model.modelid == Price.model_id).
#                   filter(Price.price >= minPrice).
#                   filter(Price.price <= maxPrice).all())
#     else:
#         models = (db.query(Model.modelid, Image.url, Model.name, CarBrand.car_brand_name, Category.name, Price.price).
#                   join(Image, Model.modelid == Image.model_id).
#                   join(CarBrand, Model.car_brand_id == CarBrand.car_brand_id).
#                   join(ModelCategory, Model.modelid == ModelCategory.modelid).
#                   join(Category, ModelCategory.categoryid == Category.categoryid).
#                   join(Price, Model.modelid == Price.model_id).
#                   filter(Category.name == nameCategory).
#                   filter(Price.price >= minPrice).
#                   filter(Price.price <= maxPrice).all())
#     processed_models = [(item[0], item[1], item[2], item[3], item[4], item[5]) for item in models]
#     return processed_models



# db = SessionLocal()
# brands = ['Chery', 'Haval', 'Geely', 'Exeed', 'Changan', 'Zeekr']
# categories = ['Седан', 'Кроссовер', 'Хэтчбек', 'Универсал', 'Внедорожник', 'Купе', 'Кабриолет', 'Пикап', 'Минивэн']
# prices = ['0', '15000000', 'asc']
# models = (db.query(Model.modelid, Image.url, Model.name, CarBrand.car_brand_name, Category.name, Price.price).
#                   join(Image, Model.modelid == Image.model_id).
#                   join(CarBrand, Model.car_brand_id == CarBrand.car_brand_id).
#                   join(ModelCategory, Model.modelid == ModelCategory.modelid).
#                   join(Category, ModelCategory.categoryid == Category.categoryid).
#                   join(Price, Model.modelid == Price.model_id).
#                   filter(CarBrand.car_brand_name.in_(brands)).
#                   filter(Category.name.in_(categories)).
#                   filter(Price.price >= prices[0]).
#                   filter(Price.price <= prices[1]).
#                   order_by(Price.price.asc()).all())
# i = 0
# for m in models:
#     print(m)
#     i += 1
# print(i)
