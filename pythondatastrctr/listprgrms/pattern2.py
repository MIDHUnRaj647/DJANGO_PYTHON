lst=[2,5,6,3]
total=0
cnt=0
lost1=list()
for i in lst:
   del lst[cnt]

   list2=lst
   total=sum(list2)
   print(total)
   cnt+=1

