import mysql.connector
from databse_connect_pgm.DB_CONNECTION2 import *
DB=sql_injection_with_python()
cursor=DB.cursor()
sql_query="insert into company (id,name,salary) values (101,'VIJAY','10000')"
try:
    cursor.execute(sql_query)
    DB.commit()
    print("succesfully inserted")
except Exception as e:
    print(e.args)
finally:
    DB.close()