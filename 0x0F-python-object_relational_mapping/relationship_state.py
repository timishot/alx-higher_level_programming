#!/usr/bin/python3
"""
Contains State class and Base, an instance of declarative_base()
"""

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base = declarative_base()


class State(Base):
    """
    Class with id and name attributes of each state
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=True, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='states', cascade='all, delete-orphan')
