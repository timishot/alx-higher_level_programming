#!/usr/bin/python3
"""
Contains State class and Base, an instance of declarative_base()
"""

from sqlalchemy import Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base


class City(Base):
    """
    Class with id and name attributes of each state
    """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
