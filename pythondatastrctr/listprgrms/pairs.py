limit=int(input('enter the number'))
lst=[1,2,3,4,6,7]
list1=list()
for i in lst:
    for j in lst:
        if i+j==limit:
            print(i,j)
            break
