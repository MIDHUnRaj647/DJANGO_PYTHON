#div(2,3) always big should come as numerator
#predefined function

# def division(Nume,Denom):
#     return Nume/Denom

#altering the function using another function
#so that bigger num will always at numerator
def divi_cnnct1(function1):
    def divi_cnnct2(num1,num2):
        if num1<num2:
            num1,num2=num2,num1
        return function1(num1,num2)
    return divi_cnnct2



@divi_cnnct1
def division(Nume,Denom):
    return Nume/Denom

res=division(1,2)
print(res)

