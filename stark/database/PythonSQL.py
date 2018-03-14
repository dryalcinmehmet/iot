import pandas as pd
from pandas import DataFrame
import os,sys
import sqlite3 as sql

driver ='SQL SERVER'
dsn = 'BDSNB3475063\SQLEXPRESS'
user= 'CLKENERJI\myalcin4'
password = ''
server= ''
database =''

connStr = ( r'DRIVER={SQL SERVER};SERVER='
            + server + ';DATABASE=' + database + ';UID='+
            user+';PWD='+password+';' +
            'Trusted_Connection=yes')
conn = sql.connect(connStr)
curs = conn.cursor()
sqli=("SELECT [Fider Adi] from osos")
df = pd.read_sql_query(sqli,conn)
df.head()

curs.execute(sqli)
d=[]
for row in curs.fetchall():
    d.append(row)