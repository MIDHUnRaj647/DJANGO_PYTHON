#age<18
age=int(input('enter the age'))
if age<18:
    raise Exception('sorry invalid age')
#'raise' is used to create customised exception

num=input("enter the no")
if type(num) != int:
    raise Exception('only integers allowed')