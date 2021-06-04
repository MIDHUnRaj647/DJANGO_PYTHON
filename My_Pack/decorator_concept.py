#decorators are used to call functions inside another functions


def sub_cnnct(function1):
    def sub_cnnct2(num1,num2):#should have the number of arguments as in the predifined functions
        if(num1<num2):
            num1,num2=num2,num1
        return function1(num1,num2)
    return sub_cnnct2

@sub_cnnct#used to call the function
#predefined function(we cannot alternate this function),thus we write another function to soleve the issue
#normally here we get an "-ve" values,
#but using decorater we avoid that problem without changing the predefined function

def subtrcn(no1,no2):
    return no1-no2
res=subtrcn(1,2)
print(res)