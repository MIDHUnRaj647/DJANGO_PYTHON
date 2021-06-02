import mysql.connector
def sql_injection_with_python():
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Password@123',
        database='cms')
    return db

