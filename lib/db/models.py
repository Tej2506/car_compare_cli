from sqlalchemy import Table, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

car_manufacturer = Table(
    'car_manufacturer',
    Base.metadata,
    Column('car_id', Integer, ForeignKey('cars.id'), primary_key = True),
    Column('manufacturer_id', Integer, ForeignKey('manufacturers.id'), primary_key = True)
)

car_feature = Table(
    'car_feature',
    Base.metadata,
    Column('car_id', Integer, ForeignKey('cars.id'), primary_key = True),
    Column('feature_id', Integer, ForeignKey('features.id'), primary_key = True)
)



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
    id = Column(Integer, primary_key = True)
    name = Column(String, nullable= False)
    
    cars = relationship('Car', secondary = car_manufacturer, back_populates = 'manufacturers')

class Feature(Base):
    __tablename__ = 'features'
    id = Column(Integer, primary_key = True)
    name = Column(String, nullable= True)
    
    cars = relationship('Car', secondary = car_feature, back_populates= 'cars')
