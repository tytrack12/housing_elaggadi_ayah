from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, Float, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#configuration de la base de données
DATABASE_URL = "mysql+pymysql://root:alexpereira@localhost/housingg"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Définir la base de données et le modèle
Base = declarative_base()

class House(Base):
    tablename = "houses"
    id = Column(Integer, primary_key=True, index=True)
    longitude = Column(Float)
    latitude = Column(Float)
    housing_median_age = Column(Integer)
    total_rooms = Column(Integer)
    total_bedrooms = Column(Integer)
    population = Column(Integer)
    households = Column(Integer)
    median_income = Column(Float)
    median_house_value = Column(Float)
    ocean_proximity = Column(String(50))

#Créer les tables
Base.metadata.create_all(bind=engine)

#Configurer FastAPI
app = FastAPI()

#Dépendance pour accéder à la base de données
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Route pour ajouter une maison
@app.post("/houses")
def add_house(house: House, db=Depends(get_db)):
    db.add(house)
    db.commit()
    db.refresh(house)
    return house

#Route pour récupérer les maisons
@app.get("/houses")
def get_houses(db=Depends(get_db)):
    return db.query(House).all()