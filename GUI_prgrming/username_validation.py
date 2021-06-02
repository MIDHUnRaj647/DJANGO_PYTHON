import mysql.connector
import sys
from databse_connect_pgm.DB_CONNECTION2 import *
from tkinter import *
from tkinter import messagebox
main=Tk()
main.geometry("300x150")
def db_connect(username,password):
    db=sql_injection_with_python()
    cursor=db.cursor()
    # sql=("select * from users where username=%s and password=%s",(uname,pwd))
    try:
        cursor.execute(("select * from users where username=%s and password=%s"),(username,password))#for an insertion query we must use "%" between thw quey and the variables
        data=cursor.fetchone()
        return data
    except Exception as e:
        print(e.args)

def Authorisation():
    uname=uname_entry.get()
    pwd=pwd_entry.get()
    data=db_connect(uname,pwd)
    try:

        if (data==None):
            print("invalid username or password, ERROR!!!!!")
            messagebox.showerror(title=Warning,message="Invalid Username/Password")
        else:
            print("authentication succesfull")
            messagebox.showinfo(title="AUTHENTICATED",message='Succesfully Authenticated')
    finally:
        sys.exit()

def Clear_btn():
    try:
        uname_entry.delete(first=0,last=END)
        pwd_entry.delete(first=0, last=END)
        print('clear button clicked')
    except Exception as e:
        print(e.args)

def Close_btn():
    try:
        main.destroy()
    except Exception as e:
        print(e.args)
    finally:
        sys.exit()

main.title("Login Page")
tframe=Frame(main)
bframe=Frame(main)
tframe.pack()
bframe.pack(side=BOTTOM)
uname=Label(main,text='username')
pwd=Label(main,text='password')
uname_entry=Entry(main)
pwd_entry=Entry(main)
uname.pack()
uname_entry.pack()
pwd.pack()
pwd_entry.pack()
btn1=Button(bframe,text='Login',fg='blue',bg='yellow',command=Authorisation)
btn2=Button(bframe,text='Clear',fg='blue',bg='yellow',command=Clear_btn)
btn3=Button(bframe,text='Close',fg='blue',bg='yellow',command=Close_btn)
btn1.pack(side=LEFT)
btn2.pack(side=RIGHT)
btn3.pack(side=RIGHT)
main.mainloop()