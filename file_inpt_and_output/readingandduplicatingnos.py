m=open('data','r')
sets=set()
for i in m:
    sets.add(i.rstrip('\n'))
print(sets)


#duplicates arre removed because set is used here, set cannot hold duplicates