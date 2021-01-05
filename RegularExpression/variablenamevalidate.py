#VARIABLE NAME RULE

#STARTING WITH a-k
#second character shouldbe a digit and it must be divisible by 3
#followed by any number of characters

from re import *
rule='[a-kA-K][369][a-zA-Z0-9]*'#each bracket specifies each letter

varname=input("enter var name")
matcher=fullmatch(rule,varname)
if matcher!=None:
    print("valid variable name")
else:
    print("invalid")
