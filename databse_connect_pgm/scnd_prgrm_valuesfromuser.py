from databse_connect_pgm.database_connecting import *
db= get_connection()

cursor=db.cursor()
name=input('enter the name of the student')
inp_id=input('enter the id of the student')
course=input('enter the coourse of the student')
#sql="insert into faculty (id,name,subject) values ('101','VIJAY','OOPS')"

try:
    cursor.execute("""insert into faculty (id,name,subject) values (%s,%s,%s)""",(inp_id,name,course))
    db.commit()#to save changes to db
    print("VAlue entered")
except Exception as e:
    print(e.args)
finally:
    db.close()