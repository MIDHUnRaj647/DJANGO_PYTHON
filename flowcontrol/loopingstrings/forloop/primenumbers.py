#the no is only divisible by 1 and the same no
# num=int(input('enter the number'))
# flag=0
# for i in range(2,num):
#     if(num%i==0):
#         flag=1
#         break
#     else:
#         flag=0
# if(flag==0):
#     print('it is prime number')
# else:
#     print('not a prime number')
lnum=int(input('enter the lower limit'))
unum=int(input('enter the upper limit'))
for i in range(lnum,unum):
    if (i>1):
        for j in range(2,i):
            if(i%j==0):
                break
        else:
                print(i)



