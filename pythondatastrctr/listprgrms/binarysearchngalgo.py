lst=[2,1,5,8,7,6,8,10,3,11]
lst.sort()
value=int(input('enter the element'))
low=0
upp=len(lst)-1
flg=0
while(low<=upp):
    mid=(low+upp)//2
    if(value>lst[mid]):
        low=mid+1
    elif(value<lst[mid]):
        upp=mid-1
    elif(value==lst[mid]):
        flg=1
        break
if(flg>0):
    print('element found')
else:
    print('element not found')