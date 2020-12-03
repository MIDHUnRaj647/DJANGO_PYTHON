lst=[2,1,3,4,6,7]
lst.sort()
low=0
upp=len(lst)-1
element=int(input('enter the element'))
while(low<upp):
    total=lst[low]+lst[upp]
    if(element<total):
        upp=upp-1
    elif(element>total):
        low=low+1
    elif(element==total):
        print('pairs are',lst[low],lst[upp])
        break