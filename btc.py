# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd 
import requests
import sqlalchemy as sql

respouse = requests.get('https://api.bitso.com/v3/trades/?book=btc_mxn')
json_respose = respouse.json()
datos = json_respose['payload']
df = pd.DataFrame(datos)
