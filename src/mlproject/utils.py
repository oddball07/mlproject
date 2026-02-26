import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql


load_dotenv()

host = os.getenv("HOST")
user = os.getenv("USER")
password = os.getenv("PASSWORD")
db_name = os.getenv("DB")

def read_sql_data():
    logging.info("Reading SQL database started")
    try:
        mydb = pymysql.connect(host=host, user=user, password=password, database=db_name)
        logging.info("SQL database connection established: %s", mydb)
        df = pd.read_sql_query('Select * from students', mydb)
        print (df.head())
        return df
    except Exception as e:
        raise CustomException(e, sys)