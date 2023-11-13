from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from database import *
from fastapi.responses import FileResponse

# app
app = FastAPI()


# set a favicon
@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse('favicon.ico')

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


@app.get("/model/{id}")
def get_model():
    return FileResponse("templates/about_model.html")


@app.get("/brand/{name}")
def get_brand():
    return FileResponse("templates/about_brand.html")


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


@app.get("/api/models/{id}")
def about_model(id, db: Session = Depends(get_db)):
    model = (db.query(Model.modelid, Image.url, Model.name, CarBrand.car_brand_name,
                      Category.name, Price.price, Description.description).
             join(Image, Model.modelid == Image.model_id).
             join(CarBrand, Model.car_brand_id == CarBrand.car_brand_id).
             join(ModelCategory, Model.modelid == ModelCategory.modelid).
             join(Category, ModelCategory.categoryid == Category.categoryid).
             join(Price, Model.modelid == Price.model_id).
             join(Description, Model.modelid == Description.model_id).
             filter(Model.modelid == id).all())
    processed_model = [(item[0], item[1], item[2], item[3], item[4], item[5], item[6]) for item in model]
    return processed_model


@app.get("/api/brands/{name}")
def about_brand(name, db: Session = Depends(get_db)):
    brand = (db.query(ManufacturerCountry.manufacturerid, ManufacturerCountry.name).
             join(BrandCountry, ManufacturerCountry.manufacturerid == BrandCountry.manufacturer_country_id).
             join(CarBrand, BrandCountry.car_brand_id == CarBrand.car_brand_id).
             filter(CarBrand.car_brand_name == name).all())
    processed_brand = [(item[0], item[1]) for item in brand]
    return processed_brand
