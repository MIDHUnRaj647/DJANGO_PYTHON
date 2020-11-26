lst=[6,6,8,9,4,2,3]
lst1=list()
lst2=list()
for i in lst:
    if i>5:
        sum=i+1
        lst1.append(sum)
    else:
        sum=i-1
        lst2.append(sum)
print(lst1,lst2)