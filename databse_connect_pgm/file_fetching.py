import mysql.connector
from databse_connect_pgm.DB_CONNECTION2 import *
db=sql_injection_with_python()
cursor=db.cursor()
sql="select * from bikes"
try:
    cursor.execute(sql)
    data=cursor.fetchall()
    for i in data:
        print("ID=",i[0])
        print("Name=",i[1])
except Exception as e:
    print(e.args)
finally:
    db.close()