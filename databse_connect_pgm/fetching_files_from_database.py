from databse_connect_pgm.database_connecting import *
db=get_connection()

cursor=db.cursor()

sql="select * from faculty"

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