# -*- coding: utf-8 -*-
"""
Spyder Editor

agrega datos a la base de datos 

This is a temporary script file.
"""

import pandas as pd 
import requests
import sqlalchemy as sql
import datetime
import time

def extract_bitso_api():
    respouse = requests.get('https://api.bitso.com/v3/trades/?book=btc_mxn')
    json_respose = respouse.json()
    datos = json_respose['payload']
    df = pd.DataFrame(datos)
    
    engine = sql.create_engine('mysql+mysqlconnector://rogersepulveda:1980@localhost/bitso_api')
    #engine = sql.create_engine('mysql+pymysql://root:Datecsa2023@localhost/bitso_api')
    
    initial_q = """INSERT INTO bitso_trades
    (book,created_at,amount,maker_side,price,tid )
    VALUES
    """
    values_q = ",".join(["""('{}','{}','{}','{}','{}','{}')""".format(
                        row.book,
                        row.created_at,
                        row.amount,
                        row.maker_side,
                        row.price,
                        row.tid) for idx, row in df.iterrows()])
    
    #print('string, tiene valor {}'.format(10))
    #for idx, row in df.iterrows():
    #    print(row)
    
    end_q = """ ON DUPLICATE KEY UPDATE
            book = values(book),
            created_at = values(created_at),
            amount = values(amount),
            maker_side = values(maker_side),
            price = values(price),
            tid = values(price);"""
            
    
    query = initial_q + values_q + end_q
    
    engine.execute(query)

    return None

while True:
    extract_bitso_api()
    print ('Actulkizando DB a las {} con registros'.format(datetime.datetime.today()) )
    time.sleep(15)


