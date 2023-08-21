#!/usr/bin/python3
"""Implementation o the State Module"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """Defines the states table on the databse"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', back_populate='state')


City.state = relationship('State', order_by=State.id, back_populates='cities')
