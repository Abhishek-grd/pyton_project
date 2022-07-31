from sqlalachemy import Column, Integer, String
from database import Base

class Addresses(Base):
    __tablename__ = "addresses"

    id = Column(Integer, Primary_key = True, index = True)
    name = Column(String)
    country = Column(String)
    company_name = Column(String)
    email = Column(String)
    phone_no = Column(Integer)
    location = Column(String)