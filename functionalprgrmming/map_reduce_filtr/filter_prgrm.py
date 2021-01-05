#filter
#fetch only even nos
lst=[2,4,6,7,8,9,10]
even=list(filter(lambda no:no%2==0,lst))
print(even)

odd=list(filter(lambda n:n%2!=0,lst))
print(odd)

names=["raju","ramu","roju","siju"]
upp=list(map(lambda name:name.upper(),names))
print(upp)
anam=list(filter(lambda name:name[0]=='s',names))
print(anam)