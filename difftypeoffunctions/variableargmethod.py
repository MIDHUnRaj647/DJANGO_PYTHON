# def add(num1,num2):
#     res=num1+num2
#     print(res)
#
# add(10,20)

#to add n no of elements in the fun we use
#variable argument method

# def add(*args):
#     total=0
#     for num in args:
#         total+=num
#     print(total)
#
# add(10,30,40)
#*args accepts in tuple format
#**args accepts in dictionary format
def printemp(**args):
    print(args)
printemp(home='kakkanad',name='ajay',working='aluva')