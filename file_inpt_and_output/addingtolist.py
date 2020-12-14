f=open("openingnames",'r')
lst=[]
for lines in f:
    lst.append(lines)
print(lst)
#removed \n
f=open("openingnames",'r')
lst=[]
for lines in f:
    lst.append(lines.rstrip('\n'))
print(lst)