stck_size=int(input('enter the stack size'))
stack=[]
top=0
n=1
def push(element):
    global top
    if(top>=stck_size):
        print('stack full')
    else:
        stack.append(element)
        top+=1
        print('push operation success')

def pop():
    global top
    if(top<=0):
        print("stack is empty")
    else:
        # stack.remove(element)
        stack.remove(stack[-1])
        top-=1
        print('element popped')
def display():
    global top
    print(stack)

while(n!=0):
    value=int(input('1---push, 2---pop, 3---display'))
    if(value==1):
        element=int(input('enter the element'))
        push(element)
    elif(value==2):
        # element=int(input('enetr the element to popp'))
        pop()
    elif(value==3):
        display()
    else:
        print('please select crrct option')

    n=int(input('press 0 to exit,other to continue'))