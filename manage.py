# -*- coding: utf-8 -*-
"""
A manage.py script to centralized all cli commands
Created on 21/10/2019
@author: Anurag
"""

# imports
import argparse

# local imports
from db.models import Base, engine


parser = argparse.ArgumentParser()

# Add the arguments
parser.add_argument('-m', metavar='--makemigration', type=str, dest='migrate', help='create the database tables')
parser.add_argument('-r', metavar='--runserver', type=str, dest='run', help='run the flask server')
parser.add_argument('-i', metavar='--ipaddress', type=str, dest='ip', help='create client license entry to auth table')
parser.add_argument('-n', metavar='--clientname', type=str, dest='name', help='add client name entry to the auth table')
parser.add_argument('-f', metavar='--flushdb', type=str, dest='flush', help='clean db by deleting all records')

# Execute the parse_args() method
args = parser.parse_args()


def migrate():
    """
    A migrate command for creating database tables
    :return:
    """
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    if args.migrate:
        migrate()
