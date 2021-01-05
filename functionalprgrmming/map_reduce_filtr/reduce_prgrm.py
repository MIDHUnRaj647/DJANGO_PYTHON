from functools import * #important saanam
lst=[1,2,3,4,5,6,7,8]
sum=(reduce(lambda  n,n1:n+n1,lst))
print(sum)
min=reduce(lambda n,n1:n if n<n1 else n1,lst)
print(min)
max=reduce(lambda n,n1:n if n>n1 else n1,lst)
print(max)
#sum,min,max

#sumofeven
sume=reduce(lambda n,n1:n+n1 ,list(filter(lambda n:n%2==0,lst)))
print(sume)

sumo=reduce(lambda n,n1:n+n1,list(filter(lambda n:n%2!=0,lst)))
print(sumo)

mine=reduce(lambda n,n1:n if n<n1 else n1,list(filter(lambda n:n%2==0,lst)))
print(mine)
