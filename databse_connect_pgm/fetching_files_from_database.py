from databse_connect_pgm.DB_CONNECTION2 import *
db=sql_injection_with_python()

cursor=db.cursor()

sql="select * from bikes"

try:
    cursor.execute(sql)
    query=cursor.fetchall()#fetchall used to call all datas, fetchone used to single value reading
    for faculty in query:
        print('id',faculty[0])
        print('name',faculty[1])
except Exception as e:
    print(e.args)
finally:
    db.close()