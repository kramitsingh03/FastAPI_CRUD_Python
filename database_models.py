from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
Base = declarative_base()

class Product(Base):

    __tablename__ = "post"

    id = Column(Integer,primary_key=True,index=True,nullable=False)
    name = Column(String,nullable=False)
    description = Column(String,nullable=False)
    price = Column(Float)
    quantity = Column(Integer)