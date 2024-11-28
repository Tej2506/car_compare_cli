#models.py
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Define the Base
Base = declarative_base()

# Define the many-to-many association table
car_features = Table(
    'car_features',
    Base.metadata,
    Column('car_id', Integer, ForeignKey('cars.id'), primary_key=True),
    Column('feature_id', Integer, ForeignKey('features.id'), primary_key=True)
)

# Engine and session setup
engine = create_engine('sqlite:///db/cars.db')
Session = sessionmaker(bind=engine)
session = Session()

# Define the Car model
class Car(Base):
    __tablename__ = 'cars'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(String)
    power = Column(String)
    torque = Column(String)
    engine = Column(String)

    manufacturer_id = Column(Integer, ForeignKey('manufacturers.id'), nullable=False)
    manufacturer = relationship('Manufacturer', back_populates='cars')
    features = relationship('Feature', secondary=car_features, back_populates='cars')

    def __repr__(self):
        return f"{self.id}: {self.name}, {self.price}, {self.power}, {self.torque}, {self.engine}"

# Define the Manufacturer model
class Manufacturer(Base):
    __tablename__ = 'manufacturers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    cars = relationship('Car', back_populates='manufacturer')

    def __repr__(self):
        return f"{self.id}: {self.name}"

# Define the Feature model
class Feature(Base):
    __tablename__ = 'features'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
    cars = relationship('Car', secondary=car_features, back_populates='features')

    def __repr__(self):
        return f"{self.id}: {self.name}"

