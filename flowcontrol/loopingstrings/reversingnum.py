num=int(input('enter the number'))#564
result=0
while(num!=0):
    digit=num%10#4
    result=result*10+digit
    num=num//10
print(result)
