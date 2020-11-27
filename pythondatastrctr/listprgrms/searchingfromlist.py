value=int(input("enter the value to be searched"))
lst=[1,2,3,4,5,6,7,8,9,10]
cnt=0
for i in lst:
        if i==value:
            print('the value is found at',cnt,"th position")
            cnt+=1
        else:
            cnt+=1
