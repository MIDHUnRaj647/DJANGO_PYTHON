num1=int(input('enter num1='))
num2=int(input('enter the scnd no='))
num3=int(input('entr the 3rd='))
if((num1>num2)&(num1>num3)):
    print('num1 is greater',num1)
    if(num2>num3):
        print('secondlargest num is num2',num2 )
        print('thus the numbers in descending order is given as ',num1,num2,num3)
    else:
        print('the second largest no is num3',num3)
        print('thus the numbers in descending order is given as ', num1, num3, num2)
elif((num2>num1)&(num2>num3)):
    print('num2 is greatre',num2)
    if (num1 > num3):
        print('secondlargest num is num1',num1)
        print('thus the numbers in descending order is given as ', num2, num1, num3)
    else:
        print('the second largest no is num3',num3)
        print('thus the numbers in descending order is given as ', num2, num3, num1)
elif((num3>num1)&(num3>num2)):
    print('num3 is greater',num3)
    if (num1 > num2):
        print('secondlargest num is num1 ',num1)
        print('thus the numbers in descending order is given as ', num3, num1, num2)
    else:
        print('the second largest no is num2',num2)
        print('thus the numbers in descending order is given as ', num3, num2, num1)
