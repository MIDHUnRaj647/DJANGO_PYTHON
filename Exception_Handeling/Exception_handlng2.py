no1=int(input('enter value for no1'))
no2=int(input('enter the value for no2'))
try:
    res=no1/no2
    print(res)
except:
    no2=int(input("enter the new value for no 2"))
    try:
        res= no1/no2
        print(res)
    except:
        no2 = int(input("enter the new value for no 2"))
        res = no1 / no2
        print(res)
finally:
    print("please change the value then only you can move on")
#finally block runs without depending the other terms