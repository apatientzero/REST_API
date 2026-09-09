from sqlalchemy.orm import Session
from . import models, schemas
from typing import Optional


def create_advertisement(db: Session, advertisement: schemas.AdvertisementCreate):
    db_advertisement = models.Advertisement(**advertisement.model_dump())
    db.add(db_advertisement)
    db.commit()
    db.refresh(db_advertisement)
    return db_advertisement


def get_advertisement(db: Session, advertisement_id: int):
    return db.query(models.Advertisement).filter(models.Advertisement.id == advertisement_id).first()


def get_advertisements(
        db: Session,
        skip: int = 0,
        limit: int = 100,
        title: Optional[str] = None,
        author: Optional[str] = None,
        min_price: Optional[float] = None,
        max_price: Optional[float] = None
):
    query = db.query(models.Advertisement)

    if title:
        query = query.filter(models.Advertisement.title.ilike(f"%{title}%"))
    if author:
        query = query.filter(models.Advertisement.author.ilike(f"%{author}%"))
    if min_price is not None:
        query = query.filter(models.Advertisement.price >= min_price)
    if max_price is not None:
        query = query.filter(models.Advertisement.price <= max_price)

    return query.offset(skip).limit(limit).all()


def update_advertisement(db: Session, advertisement_id: int, advertisement: schemas.AdvertisementUpdate):
    db_advertisement = db.query(models.Advertisement).filter(models.Advertisement.id == advertisement_id).first()
    if not db_advertisement:
        return None

    update_data = advertisement.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_advertisement, key, value)

    db.commit()
    db.refresh(db_advertisement)
    return db_advertisement


def delete_advertisement(db: Session, advertisement_id: int):
    db_advertisement = db.query(models.Advertisement).filter(models.Advertisement.id == advertisement_id).first()
    if not db_advertisement:
        return None

    db.delete(db_advertisement)
    db.commit()
    return db_advertisement