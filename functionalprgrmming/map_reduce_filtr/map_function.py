lst=[10,11,12,13,14,15]
#squares
#map(function,iterables)
#def squ(no):
    #return no**2   (by using lambda we can reduce this part)
squares=list(map(lambda no:no**2,lst))
print(squares)

cubes=list(map(lambda no:no**3,lst))
print(cubes)