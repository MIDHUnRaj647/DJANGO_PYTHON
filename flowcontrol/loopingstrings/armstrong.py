#if 135 is the inputted value then armstrong no is 1**3 + 3**3 + 5**3
num=int(input('enter the number'))
result=0
while(num!=0):
    digit = num % 10
    result = result + (digit**3)
    num = num // 10
print(result)