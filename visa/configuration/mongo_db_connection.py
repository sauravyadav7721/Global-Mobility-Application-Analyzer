import sys
from visa.exception import USvisaException
from visa.logger import logging
import os
from visa.constants import MONGODB_URL_KEY, DATABASE_NAME
import pymongo
import certifi

ca = certifi.where()


class MangoDBClient:
    client = None
    def __init__(self,database_name=DATABASE_NAME) -> None:
        try:
            if MangoDBClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)
                if mongo_db_url is None:
                    raise Exception(f"Environmet key: {MONGODB_URL_KEY} is not set.")
                MangoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            self.client = MangoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            logging.info(f"Connected to MongoDB database: {database_name}")
        except Exception as e:
            raise USvisaException(e, sys) 