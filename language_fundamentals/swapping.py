#1
num1=10
num2=20
print("values before swapping num1=",num1,"num2=",num2)
num3=num1
num1=num2
num2=num3
print("values after swapping num1=",num1,"num2",num2)
#2
num1=10
num2=20
print("values before swapping num1=",num1,"num2=",num2)
(num1,num2)=(num2,num1)
print("values after swapping num1=",num1,"num2",num2)
#3
num1=10
num2=20
print("values before swapping num1=",num1,"num2=",num2)
num1=num1+num2
num2=num1-num2
num1=num1-num2
print("values after swapping num1=",num1,"num2",num2)