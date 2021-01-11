# -*- coding: utf-8 -*-
"""
A manage.py script to centralized all cli commands
Created on 21/10/2019
@author: Anurag
"""

# imports
import argparse

# local imports
from db.models import AuthUserModel, db
from db.threat_orm import threat_db
from settings import HOST, PORT
from api.views import app

parser = argparse.ArgumentParser()

# Add the arguments
parser.add_argument('-m', metavar='--makemigration', type=str, dest='migrate', help='create the database tables')
parser.add_argument('-r', metavar='--runserver', type=str, dest='run', help='run the flask server')
parser.add_argument('-i', metavar='--ipaddress', type=str, dest='ip', help='create client license entry to auth table')
parser.add_argument('-n', metavar='--clientname', type=str, dest='name', help='add client name entry to the auth table')
parser.add_argument('-f', metavar='--flushdb', type=str, dest='flush', help='clean db by deleting all records')

# Execute the parse_args() method
args = parser.parse_args()
app.app_context().push()


def migrate():
    """
    A migrate command for creating database tables
    :return:
    """
    db.init_app(app)
    db.create_all()
    db.session.commit()


def add_license():
    """
    A function to add api key to the client details table
    :return:
    """
    client = AuthUserModel(client_ip=args.ip, client_name=args.name)
    db.session.add(client)
    db.session.commit()


def flush_db():
    """
    Clear out all tables
    :return:
    """
    threat_db.flush_cve()
    threat_db.flush_ip()
    threat_db.flush_url()
    threat_db.flush_malware_hash()
    threat_db.flush_revision_tracker()


def runserver():
    """
    For running flask server
    :return:
    """
    app.run(host=HOST, port=PORT)


if __name__ == '__main__':
    if args.migrate:
        migrate()
    elif args.run:
        runserver()
    elif args.ip and args.name:
        add_license()
    elif args.flush:
        flush_db()
    else:
        runserver()
