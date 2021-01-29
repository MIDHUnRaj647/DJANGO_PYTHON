#exception
no1=int(input('enter value for no1'))
no2=int(input('enter the value for no2'))
try:
    res=no2/no2

    print(res)#when 10/0 apply, the program stops here then the other statements after this does not work, this is called exception
    print("i have one datbse")
    print("i have one file trnsctn")
except:
    print("exception occured")

#by using 'try' 'except' we can avoid exception handling
#inside 'try' block
   # we input doubtfull code

#inside 'except' block
   # other part of prgrming

#you can have any no of 'try' and 'except'
#if 'try' worked , the 'except' not works
#if 'try' not worked then 'except' works
no4=int(input('enter value for no4'))
no3=int(input('enter the value for no3'))
try:
    res=no4/no3

    print(res)#when 10/0 apply, the program stops here then the other statements after this does not work, this is called exception
    print("i have one datbse")
    print("i have one file trnsctn")
except Exception as e:
    print(e.args)#by providing this term we can get the detailed error cause report
    print("exception occured")