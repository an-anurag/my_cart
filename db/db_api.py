# -*- coding: utf-8 -*-
"""
THIS MODULE IS NOT LONGER IN USE
A database API for project
Created on 10/9/2019
@author: Anurag
"""

# global imports
import sys
import sqlite3

# third party imports
try:
    from mysql.connector import connect
    from mysql.connector.errors import ProgrammingError, DatabaseError, InterfaceError, OperationalError
except ImportError:
    sys.exit("You need python mysql connector module installed")

# local imports
from common.logger import logger


class ThreatDB:
    """
    A class for implementing database interacting functionality
    """
    def __init__(self, host, database, user, password, table_name):
        self._host = host
        self._database = database
        self._user = user
        self._password = ""
        self.table_name = table_name
        if password is not None:
            self._password = password
        self._conn = None
        self._connected = False

    def connect(self):
        """
        Method to connect with MySQL database
        :return: connection object
        """
        try:
            self._conn = connect(host=self._host, database=self._database, user=self._user, password=self._password, use_pure=False)
            self._conn.autocommit = True
            self._connected = True
            logger.info("Database connection successful")
        except Exception as e:
            logger.info("Can't connect to database (%s@%s) error: %s" % (self._user, self._host, e))
        return self._conn

    def exec_query(self, query, params=None):
        """
        Method to execute given database query
        :param query: SQL query in string
        :param params: optional parameters for wuery
        :return: None
        """
        try:
            if not self._connected or self._conn is None:
                self.connect()
            cursor = self._conn.cursor()
            cursor.execute(query, params)
            return cursor
        except OperationalError as err:
            logger.debug('MySQL Operational Error executing query:\n----> %s \n----> %s' % (query, err))
            if err != 2006:
                logger.error('MySQL Operational Error executing query')
        except Exception as e:
            logger.error('Error executing query:\n----> [{0}]'.format(e))

    def close(self):
        """Method to close mysql database connection"""
        if self._conn:
            try:
                self._conn.close()
                logger.info("Database connection closed")
            except ProgrammingError as err:
                logger.error("Error while closing the connection: {}".format(err))
            except AttributeError as err:
                logger.info("Trying to close the connection to mysql: {}".format(err))
            except Exception as err:
                logger.error("Can't close the connection to the database: {}".format(err))
            finally:
                self._conn = None
                self._connected = False
        else:
            logger.info("Trying to execute close method on connection which doesn't exist")
