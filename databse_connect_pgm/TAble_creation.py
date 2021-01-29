import mysql.connector
#calling earlier created function

from databse_connect_pgm.database_connecting import *


db = get_connection()
cursor =db.cursor()

sql ="create table faculty (id varchar(25),name varchar(100),subject varchar(50))"
try:
    cursor.execute(sql)
    print("table succesfully created")
except Exception as e:
    print(e.args)
finally:
    db.close()