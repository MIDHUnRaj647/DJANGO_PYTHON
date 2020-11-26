# limit=int(input('enter the limit'))
# lst=lst()
# for i in range(1,limit+1):
#     lst.append(i)
# print(lst)

limit=int(input('enter the limit'))
lst1=list()
lst2=list()
for i in range(1,limit+1):
    if (i%2==0):
        lst1.append(i)
    else:
        lst2.append(i)
print(lst1,lst2)