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
