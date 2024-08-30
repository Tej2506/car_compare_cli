from sqlalchemy import Table, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Car(Base):
    __tablename__ = 'cars'
    id = Column(Integer, primary_key = True)
    name = Column(String, nullable = False)
    price = Column(Integer)
    horspower = Column(Integer)
    manufacturers = relationship('Manufacturer', secondary = car_manufacturer, back_populates = 'cars')
    features = relationship('Feature', secondary = car_feature, back_populates= 'cars')

class Manufacturer(Base):
    __tablename__ = 'manufacturers'
    id = Column(Integer, orimary_key = True)
    name = Column(String,nullable= False)
    cars = relationship('Car', secondary = car_manufacturer, back_populates = 'manufacturers')