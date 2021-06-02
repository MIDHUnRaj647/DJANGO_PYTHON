import mysql.connector
from databse_connect_pgm.DB_CONNECTION2 import *
database=sql_injection_with_python()
cursor=database.cursor()
sql_query="create table COMPANY (ID int, NAME varchar(500),SALARY varchar(50))"
try:
    cursor.execute(sql_query)
    print('THE TABLE IS SUCCESFULLY CREATED')
except Exception as e:
        print(e.args)
finally:
    database.close()