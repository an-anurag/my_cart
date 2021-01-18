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

    __tablename__ = conf.read('DB_TABLES', 'user')
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    username = Column('username', String(16), nullable=False)
    first_name = Column('first_name', String(16), nullable=True)
    last_name = Column('last_name', String(16), nullable=True)
    email = Column('email', String(16), nullable=True)
    password = Column('password', String(16), nullable=False)
    user_type = Column('user_type', String(16), nullable=True)
    # is_active = Column('is_active', Boolean, default=expression.true())
    created_on = Column('created_on', DateTime, server_default=func.now())
    updated_on = Column('updated_on', DateTime, onupdate=func.now())

    def __str__(self):
        """
        Object String representation
        :return:
        """
        return str(self.first_name + self.last_name)


class Category(Base):
    """
    A database model for client_details table
    """

    __tablename__ = conf.read('DB_TABLES', 'category')
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(16), nullable=True)
    # is_active = Column('is_active', Boolean, nullable=False, default=True)
    created_on = Column('created_on', DateTime, server_default=func.now())
    updated_on = Column('updated_on', DateTime, onupdate=func.now())

    products = relationship("Product", backref=backref("category"))

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

    __tablename__ = conf.read('DB_TABLES', 'product')
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(16), nullable=True)
    category_id = Column("category_id", Integer, ForeignKey("category.id")),
    description = Column('description', String(16), nullable=True)
    price = Column('price', String(16), nullable=True)
    # is_active = Column('is_active', Boolean, nullable=False, default=True)
    created_on = Column('created_on', DateTime, server_default=func.now())
    updated_on = Column('updated_on', DateTime, onupdate=func.now())

    def __str__(self):
        """
        Object String representation
        :return:
        """
        return str(self.name)


# Category.products = relationship("Product", order_by=Product.id, back_populates="category")


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


"""
CREATE if not exists TABLE product (
        id INTEGER NOT NULL,
        name VARCHAR(16),
        description VARCHAR(16),
        price VARCHAR(16),
        created_on DATETIME DEFAULT (CURRENT_TIMESTAMP),
        updated_on DATETIME,
        PRIMARY KEY (id),
        FOR
);


"""