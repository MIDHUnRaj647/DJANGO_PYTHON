
# for i in range(1,5):#i=0
#     for j in range (0,i):#j(0,4)
#         print(j,end=' ')
#     print()

# for i in range(1,5):#i=0
#     for j in range (0,i):#j(0,4)
#         print('*',end=' ')
#     print()

for row in range(1,5):
    for col in range(1,8):
        if (row==4 or row+col==5 or col-row==3):
            print('*',end='')
        else:
            print(end=' ')
    print()
