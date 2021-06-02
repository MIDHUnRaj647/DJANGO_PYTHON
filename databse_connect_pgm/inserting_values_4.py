import mysql.connector
from databse_connect_pgm.DB_CONNECTION2 import *
db3=sql_injection_with_python()
cursor=db3.cursor()
sql_query="insert into bikes (id,name,company) values (102,'pulsar','bajaj')"
try:
    cursor.execute(sql_query)
    db3.commit()
    print("inserted succesfully")
except Exception as e:
    print(e.args)
finally:
    db3.close()