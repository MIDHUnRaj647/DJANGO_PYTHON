import mysql.connector
from databse_connect_pgm.DB_CONNECTION2 import *
# db=sql_injection_with_python()
# cursor=db.cursor()
n = 115
for m in range(1,1000000):
    db = sql_injection_with_python()
    cursor = db.cursor()
    id = n
    name=input("Enter the company name")
    model=input("Enter the model name")
# sql2="""insert into bikes (id,name,company) values (%s,%s,%s)""",(id,model,name)
    try:
        cursor.execute("""insert into bikes (id,name,company) values (%s,%s,%s)""",(id,model,name))
    # cursor.execute(sql2)
        db.commit()
        print("succesfully inserted")

    except Exception as e:
        print(e.args)
    finally:
        n=n+1
        num=input("Press 'x' to close, Press anykey to continue")
        if(num!='x'):
            db.close()
        else:
            break