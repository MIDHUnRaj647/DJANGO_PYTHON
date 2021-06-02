import mysql.connector
from databse_connect_pgm.DB_CONNECTION2 import *
db=sql_injection_with_python()
cursor=db.cursor()
sql_query="create table bikes(ID int, NAME varchar(500),company varchar(50))"
try:
    cursor.execute(sql_query)
    print("table successfully created")
except Exception as e:
    print(e.args)
finally:
    db.close()