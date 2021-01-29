from databse_connect_pgm.database_connecting import *
db= get_connection()

cursor=db.cursor()

sql="insert into faculty (id,name,subject) values ('101','VIJAY','OOPS')"

try:
    cursor.execute(sql)
    db.commit()
    print("query executed")
except Exception as e:
    print(e.args)
finally:
    db.close()