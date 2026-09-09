from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional
from . import crud, schemas, models
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Advertisement Service", version="1.0.0")

@app.post("/advertisement", response_model=schemas.AdvertisementResponse, status_code=201)
def create_advertisement(advertisement: schemas.AdvertisementCreate, db: Session = Depends(get_db)):
    return crud.create_advertisement(db=db, advertisement=advertisement)

@app.get("/advertisement/{advertisement_id}", response_model=schemas.AdvertisementResponse)
def get_advertisement(advertisement_id: int, db: Session = Depends(get_db)):
    db_advertisement = crud.get_advertisement(db, advertisement_id=advertisement_id)
    if db_advertisement is None:
        raise HTTPException(status_code=404, detail="Advertisement not found")
    return db_advertisement

@app.get("/advertisement", response_model=list[schemas.AdvertisementResponse])
def get_advertisements(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    title: Optional[str] = Query(None),
    author: Optional[str] = Query(None),
    min_price: Optional[float] = Query(None, ge=0),
    max_price: Optional[float] = Query(None, ge=0),
    db: Session = Depends(get_db)
):
    return crud.get_advertisements(
        db,
        skip=skip,
        limit=limit,
        title=title,
        author=author,
        min_price=min_price,
        max_price=max_price
    )

@app.patch("/advertisement/{advertisement_id}", response_model=schemas.AdvertisementResponse)
def update_advertisement(
    advertisement_id: int,
    advertisement: schemas.AdvertisementUpdate,
    db: Session = Depends(get_db)
):
    db_advertisement = crud.update_advertisement(db, advertisement_id=advertisement_id, advertisement=advertisement)
    if db_advertisement is None:
        raise HTTPException(status_code=404, detail="Advertisement not found")
    return db_advertisement

@app.delete("/advertisement/{advertisement_id}", response_model=schemas.AdvertisementResponse)
def delete_advertisement(advertisement_id: int, db: Session = Depends(get_db)):
    db_advertisement = crud.delete_advertisement(db, advertisement_id=advertisement_id)
    if db_advertisement is None:
        raise HTTPException(status_code=404, detail="Advertisement not found")
    return db_advertisement