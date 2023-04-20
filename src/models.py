import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = "User"
    id = Column(Integer, primary_key=True)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), unique=False, nullable=False)
    is_active = Column(Boolean, unique=False, nullable=False)
    photo = Column(String(240), unique=True, nullable=True)
    name = Column(String(25), unique=False, nullable=False)
    last_name = Column(String(50), unique=False, nullable=False)
    address = Column(String(150), unique=False, nullable=False)
    city = Column(String(35), unique=False, nullable=False)
    postal_code = Column(Integer, unique=False, nullable=False)
    country = Column(String(50), unique=False, nullable=False)
    birthdate = Column(Date, unique=False, nullable=False)
    phone_number = Column(Integer, unique=False, nullable=False)

    asistant = relationship("Cuidador", back_populates="user")
    owner = relationship("Propietario", back_populates="user")



class Cuidador(Base):
    __tablename__ = "Cuidador"
    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("User.id"))

    user = relationship("User", back_populates="asistant")
    tarif = relationship("Tarifas", back_populates="cost")


class Servicios(Base):
    __tablename__ = "Servicios"
    id = Column(Integer, primary_key=True)
    image = Column(String(240), unique=True, nullable=False)
    title = Column(String(35), unique=True, nullable=False)
    description = Column(String(500), unique=True, nullable=False)

    cuidador_id = Column(Integer, ForeignKey("Cuidador.id"))

    tarif = relationship("Tarifas", back_populates="service")


class Tarifas(Base):
    __tablename__ = "Tarifas"
    id = Column(Integer, primary_key=True)
    price = Column(Integer, unique=False, nullable=False)

    cuidador_id = Column(Integer, ForeignKey("Cuidador.id"))
    servicios_id = Column(Integer, ForeignKey("Servicios.id"))

    cost = relationship("Cuidador", back_populates="tarif")
    service = relationship("Servicios", back_populates="tarif")



class Propietario(Base):
    __tablename__ = "Propietario"
    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("User.id"))
    dog_id = Column(Integer, ForeignKey("Dog.id"))

    pet = relationship("Dog", back_populates="owner")
    user = relationship("User", back_populates="owner")



class Dog(Base):
    __tablename__ = "Dog"
    id = Column(Integer, primary_key=True)
    name = Column(String(35), unique=False, nullable=False)
    photo = Column(String(240), unique=True, nullable=True)
    breed = Column(String(50), unique=False, nullable=False)
    birthdate = Column(Date, unique=False, nullable=False)
    sex = Column(String(20), unique=False, nullable=False)
    dog_size = Column(String(20), unique=False, nullable=True)
    sterilized = Column(Boolean, unique=False, nullable=False)
    social_cats = Column(Boolean, unique=False, nullable=False)
    social_kids = Column(Boolean, unique=False, nullable=False)
    social_dogs = Column(Boolean, unique=False, nullable=False)
    microchip = Column(Integer, unique=True, nullable=False)
    activity_level = Column(String(20), unique=False, nullable=True)
    observations = Column(String(500), unique=False, nullable=True)

    propietario_id = Column(Integer, ForeignKey("Propietario.id"))

    owner = relationship("Propietario", back_populates="pet")


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
