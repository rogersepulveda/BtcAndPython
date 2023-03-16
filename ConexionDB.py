# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 18:01:24 2023

Lee los datos de la base de datos 

@author: roger
"""

import pandas as pd 
import requests
import sqlalchemy as sql

engine = sql.create_engine('mysql+mysqlconnector://rogersepulveda:1980@localhost/bitso_api')

query = 'SELECT * FROM bitso_trades'
df = pd.read_sql(query,engine)