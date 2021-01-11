# -*- coding: utf-8 -*-
"""
Database models for this project
Created on 21/10/2019
@author: Anurag
"""

# imports
import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, Table, Boolean, TIMESTAMP
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import text, func
from common.config import conf
from utils.date import dump_datetime

Base = declarative_base()


class User(Base):
    """
    A database model for client_details table
    """

    __tablename__ = conf.read('DB_TABLES', 'user')
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    first_name = Column('first_name', String(16), nullable=True)
    last_name = Column('last_name', String(16), nullable=True)
    email = Column('email', String(16), nullable=True)
    password = Column('password', String(16), nullable=True)
    user_type = Column('user_type', String(16), nullable=True)
    is_active = Column('is_active', Boolean, nullable=False, default=1)
    created_on = Column('created_on', TIMESTAMP, nullable=False, server_default=func.now())
    updated_on = Column('updated_on', TIMESTAMP, nullable=False,
                           server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))

    def __str__(self):
        """
        Object String representation
        :return:
        """
        return str(self.first_name + self.last_name)


class Product(Base):
    """
    A database model for client_details table
    """

    __tablename__ = conf.read('DB_TABLES', 'product')
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(16), nullable=True)
    category = Column("category_id", Integer, ForeignKey("category.category_id")),
    description = Column('description', String(16), nullable=True)
    price = Column('price', String(16), nullable=True)
    is_active = Column('is_active', Boolean, nullable=False, default=1)
    created_on = Column('created_on', TIMESTAMP, nullable=False, server_default=func.now())
    updated_on = Column('updated_on', TIMESTAMP, nullable=False,
                           server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))

    def __str__(self):
        """
        Object String representation
        :return:
        """
        return str(self.first_name + self.last_name)


class CategoryMaster(Base):
    """
    A database model for client_details table
    """

    __tablename__ = conf.read('DB_TABLES', 'category_master')
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('first_name', String(16), nullable=True)
    is_active = Column('is_active', Boolean, nullable=False, default=1)
    created_on = Column('created_on', TIMESTAMP, nullable=False, server_default=func.now())
    updated_on = Column('updated_on', TIMESTAMP, nullable=False,
                           server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))

    def __str__(self):
        """
        Object String representation
        :return:
        """
        return str(self.first_name + self.last_name)


class Cart(Base):
    """
    A database model for client_details table
    """

    __tablename__ = conf.read('DB_TABLES', 'cart')
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    order = Column('first_name', String(16), nullable=True)
    last_name = Column('last_name', String(16), nullable=True)
    email = Column('email', String(16), nullable=True)
    password = Column('password', String(16), nullable=True)
    user_type = Column('user_type', String(16), nullable=True)
    is_active = Column('is_active', Boolean, nullable=False, default=1)
    created_on = Column('created_on', TIMESTAMP, nullable=False, server_default=func.now())
    updated_on = Column('updated_on', TIMESTAMP, nullable=False,
                           server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))

    def __str__(self):
        """
        Object String representation
        :return:
        """
        return str(self.first_name + self.last_name)


class Bill(Base):
    """
    A database model for client_details table
    """

    __tablename__ = conf.read('DB_TABLES', 'bill')
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    first_name = Column('first_name', String(16), nullable=True)
    last_name = Column('last_name', String(16), nullable=True)
    email = Column('email', String(16), nullable=True)
    password = Column('password', String(16), nullable=True)
    user_type = Column('user_type', String(16), nullable=True)
    is_active = Column('is_active', Boolean, nullable=False, default=1)
    created_on = Column('created_on', TIMESTAMP, nullable=False, server_default=func.now())
    updated_on = Column('updated_on', TIMESTAMP, nullable=False,
                           server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))

    def __str__(self):
        """
        Object String representation
        :return:
        """
        return str(self.first_name + self.last_name)


class Order(Base):
    """
    A database model for client_details table
    """

    __tablename__ = conf.read('DB_TABLES', 'order')
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    first_name = Column('first_name', String(16), nullable=True)
    last_name = Column('last_name', String(16), nullable=True)
    email = Column('email', String(16), nullable=True)
    password = Column('password', String(16), nullable=True)
    user_type = Column('user_type', String(16), nullable=True)
    is_active = Column('is_active', Boolean, nullable=False, default=1)
    created_on = Column('created_on', TIMESTAMP, nullable=False, server_default=func.now())
    updated_on = Column('updated_on', TIMESTAMP, nullable=False,
                           server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))

    def __str__(self):
        """
        Object String representation
        :return:
        """
        return str(self.first_name + self.last_name)
