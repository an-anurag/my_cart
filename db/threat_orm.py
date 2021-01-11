# -*- coding: utf-8 -*-
"""
A database API for project
Created on 10/9/2019
@author: Anurag
"""

# imports
import time
import datetime

# local imports
from api.views import app
from common.logger import logger
from db.models import CVEModel, BadIPs, MalwareHash, MalwareURLs, RevisionTracker, db

app.app_context().push()


class ThreatDB:
    """
    A class for implementing database interacting functionality
    """

    def __init__(self):
        """
        Constructor
        """
        self.conn = db.engine

    def close_db(self):
        """
        Close db connection
        :return:
        """
        db.session.close()
        self.conn.dispose()

    def get_total_cve(self):
        """
        A sql query to get total count from cve table
        :return: query
        """
        total = CVEModel.query.count()
        return total

    def get_total_ip(self):
        """
        A sql query to get total count from ip table
        :return: query
        """
        total = BadIPs.query.count()
        return total

    def get_total_mal_hashes(self):
        """
        A sql query to get total count from ip table
        :return: query
        """
        total = MalwareHash.query.count()
        return total

    def get_total_url(self):
        """
        A sql query to get total count from url table
        :return: query
        """
        total = MalwareURLs.query.count()
        return total

    def get_ransom_count(self):
        """
        A sql query to get ransomware threat type count from the table
        :return: query
        """
        ransom = MalwareURLs.query.filter_by(threat_type='ransomware').count()
        return ransom
    
    def flush_ip(self):
        """
        A method to truncate ip table
        """
        try:
            BadIPs.query.delete()
            db.session.commit()
        except Exception as err:
            logger.exception(err)

    def flush_url(self):
        """
        A method to truncate url table
        """
        try:
            MalwareURLs.query.delete()
            db.session.commit()
        except Exception as err:
            logger.exception(err)
        
    def flush_cve(self):
        """
        A method to truncate cve table
        """
        try:
            CVEModel.query.delete()
            db.session.commit()
        except Exception as err:
            logger.exception(err)

    def flush_malware_hash(self):
        """
        A method to truncate malware_hash table
        """
        try:
            MalwareHash.query.delete()
            db.session.commit()
        except Exception as err:
            logger.exception(err)

    def flush_revision_tracker(self):
        """
        A method to truncate malware_hash table
        """
        try:
            RevisionTracker.query.delete()
            db.session.commit()
        except Exception as err:
            logger.exception(err)

    def write_first_revision_for_tracker(self):
        """
        A method to write revision for thr first time
        :return:
        """
        ts = time.time()
        timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        RevisionTracker.query.delete()
        db.session.commit()
        rev = RevisionTracker(last_revision=1, updated_on=timestamp)
        db.session.add(rev)
        db.session.commit()


threat_db = ThreatDB()
