import mysql.connector
from databse_connect_pgm.DB_CONNECTION2 import *
db=sql_injection_with_python()
cursor=db.cursor()
sql="create table CARS (ID int, NAME varchar(500),COMPANY varchar(50))"
try:
    cursor.execute(sql)
    print("table succesfully created")
except Exception as e:
    print(e.args)
finally:
    db.close()