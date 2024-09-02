from sqlalchemy import Table, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = create_engine('sqlite:///db/cars.db')

Session = sessionmaker(bind=engine)
session = Session()



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
    price = Column(String)
    power = Column(String)
    torque = Column(String)
    engine = Column(String)

    
    manufacturers = relationship('Manufacturer', secondary = car_manufacturer, back_populates = 'cars')
    features = relationship('Feature', secondary = car_feature, back_populates= 'cars')

    def __repr__(self):
        return f"{self.id}: {self.name}, {self.price}, {self.power}, {self.torque}, {self.engine}"

class Manufacturer(Base):
    __tablename__ = 'manufacturers'
    id = Column(Integer, primary_key = True)
    name = Column(String, nullable= False)
    
    cars = relationship('Car', secondary = car_manufacturer, back_populates = 'manufacturers')
    
    def __repr__(self):
        return f"{self.id}: {self.name}"
class Feature(Base):
    __tablename__ = 'features'
    id = Column(Integer, primary_key = True)
    name = Column(String, nullable= True)
    
    cars = relationship('Car', secondary = car_feature, back_populates= 'features')
