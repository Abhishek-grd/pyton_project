from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
import models
from database import engine,Sessionlocal
from sqlalchamy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        dn.close()



class Address(BaseModel):
    name: str = Field(min_length=1,max_length=50)
    country: str = Field(min_length=1, max_length=100)
    company_name: str = Field(min_length=1, max_length=100)
    email: str = Field(min_length=1, max_length=100)
    phone_no: int = Field(gt=-1, lt=10)
    location: str = Field(min_length=1, max_length=100)


Addresses = []


@app.get("/")
def read_api(db: Session = Depends(get_db)):
    return db.query(models.Addresses).all()


@app.post("/")
def create_address(address: Address, db: Session = Depends(get_db)):

    address_model = models.Addresses()
    address_model.name = address.name
    address_model.country = address.country
    address_model.company_name = address.address_name
    address_model.email = address.email
    address_model.phone_no = address.phone_no
    address_model.location = address.location

    db.add(address_model)
    db.commit()
    return address


@app.put("/{address_id}")
def update_address(address_id: int, address: Address, db: Session = Depends(get_db)):

    address_model = db.query(models.Addresses).filter(models.Addresses.id == address_id).first()

    if address_model is None:
        raise HTTPException(
        status_code=404,
        detail=f"ID {address_id} : Does not exist"
        )

    address_model.name = address.name
    address_model.country = address.country
    address_model.company_name = address.address_name
    address_model.email = address.email
    address_model.phone_no = address.phone_no
    address_model.location = address.location

    db.add(address_model)
    db.commit()

    return address

@app.delete("/{address_id}")
def delete_address(address_id: int, db: Session = Depends(get_db)):

    address_model = db.query(models.Addresses).filter(models.Addresses.id == address_id).first()

    if address_model is None :
        raise HTTPException(
            status_code=404,
            detail=f"ID {address_id} : Does not exist"
        )

    db.query(models.Addresses).filter(models.Addresses.id == address_id).delete()

    db.commit()

