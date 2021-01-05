first=[1,2,3]
second=[4,5,6]
pairs=[(i,j) for i in first for j in second]
print(pairs)
#squares
squares=[i**2 for i in first]
print(squares)

#connditioning using list comprehension

fir=[1,2,3,4,5,6,7]
data=[i-1 if i<5 else i+1 for i in fir]
print(data)

#using elif

data=[i+1 if i>5 else i-1 if i<5 else 5  for i in fir ]
print(data)

#input matrix flatten operation
matrix=[[1,2,3],[4,5,6],[7,8,9]]
flat=[j for i in matrix for j in i]
print(flat)