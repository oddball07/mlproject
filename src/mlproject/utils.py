import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

host = os.getenv("HOST")
user = os.getenv("USER")
password = os.getenv("PASSWORD")
db_name = os.getenv("DB")

def read_sql_data():
