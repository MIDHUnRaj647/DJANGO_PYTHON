#step 1 ---- import mysql package
#step 2 ---- establish connection -u and -p
#step 3 ---- creating curser object
#step 4 ---- excecute queris
#close database connection
import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password@123",auth_plugin="mysql_native_password"
)

cursor=db.cursor()
#eg work
sql='SELECT VERSION()'
cursor.execute(sql)
data=cursor.fetchone()
print(data)