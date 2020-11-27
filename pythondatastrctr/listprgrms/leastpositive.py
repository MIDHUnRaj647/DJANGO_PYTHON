lst=[-2,-1,0,1,2,6,4]
min=1
for i in range(0,len(lst)):
    if min in lst:
        min+=1
    else:
        print(min,'is the least +ve intgr')
        break