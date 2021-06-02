import mysql.connector
from databse_connect_pgm.DB_CONNECTION2 import *
db2=sql_injection_with_python()
cursor=db2.cursor()
sql_query3="insert into cars (id,name,company) values (101,'apache','TVS')"
try:
    cursor.execute(sql_query3)
    db2.commit()
    print("inserted succesfully")
except Exception as e:
    print(e.args)
finally:
    db2.close()