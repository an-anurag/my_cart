# -*- coding: utf-8 -*-
"""
Database models for this project
Created on 21/10/2019
@author: Anurag
"""

# imports
import os
import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy import Column, Integer, String, ForeignKey, Table, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import text, func, expression


from config import conf

Base = declarative_base()
path = os.path.dirname(os.path.dirname(__file__)) + '/my_cart.db'
engine = create_engine('sqlite:///' + path)
DBSession = sessionmaker(bind=engine)
session = DBSession()


class User(Base):
    """
    A database model for client_details table
    """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    email = Column(String)
    password = Column(String)
    usertype = Column(String)

    addresses = relationship("Address", back_populates='user', cascade="all, delete, delete-orphan")

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (self.name, self.fullname, self.email)


class Address(Base):

    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="addresses")

    def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address


class Category(Base):
    """
    A database model for client_details table
    """

    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)

    products = relationship("Product", back_populates='category', cascade="all, delete, delete-orphan")

    def __repr__(self):
        """
        Object String representation
        :return:
        """
        return str(self.name)


class Product(Base):
    """
    A database model for client_details table
    """

    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
    description = Column(String, nullable=True)
    price = Column(String, nullable=True)

    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship("Category", back_populates="products")

    def __repr__(self):
        """
        Object String representation
        :return:
        """
        return str(self.name)


class Cart(Base):
    """
    A database model for client_details table
    """

    __tablename__ = conf.read('DB_TABLES', 'cart')
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    order = Column("order_id", Integer, ForeignKey("order.order_id")),
    products = Column("product_id", Integer, ForeignKey("products.product_id")),
    # is_active = Column('is_active', Boolean, nullable=False, default=True)
    created_on = Column('created_on', DateTime, server_default=func.now())
    updated_on = Column('updated_on', DateTime, onupdate=func.now())

    def __repr__(self):
        """
        Object String representation
        :return:
        """
        return str(self.id)


class Bill(Base):
    """
    A database model for client_details table
    """

    __tablename__ = conf.read('DB_TABLES', 'bill')
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    order = Column("order_id", Integer, ForeignKey("order.order_id")),
    # is_active = Column('is_active', Boolean, nullable=False, default=True)
    created_on = Column('created_on', DateTime, server_default=func.now())
    updated_on = Column('updated_on', DateTime, onupdate=func.now())

    def __repr__(self):
        """
        Object String representation
        :return:
        """
        return str(self.id)


class Order(Base):
    """
    A database model for client_details table
    """

    __tablename__ = conf.read('DB_TABLES', 'order')
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    # is_active = Column('is_active', Boolean, nullable=False, default=True)
    created_on = Column('created_on', DateTime, server_default=func.now())
    updated_on = Column('updated_on', DateTime, onupdate=func.now())

    def __repr__(self):
        """
        Object String representation
        :return:
        """
        return str(self.id)
