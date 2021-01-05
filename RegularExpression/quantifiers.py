#quantifiers

from re import *
pattern='a+' #check for 'a' and occurances of 'a'
pattern1='a'
pattern2='a*'#a+ plus zero occurance of a
pattern3="a?" #a plus zero number of a
pattern4="^a"#check for starting with a
pattern5="a$"#ending with a
pattern6='a{2,3}'#chk for minimum 2 a and maximum 3
#FINDITER
matcher=finditer(pattern6,'aaaabaabaaaaa')
for match in matcher:
    print(match.start())
    print(match.group())
#FULL MATCH METHOD

pattern7="^a"
matcher1=fullmatch(pattern7,'aaaabaabaaaaa')
if matcher1!=None: 
    print("given string starting with a")
else:
    print("given string is not starting with a")
