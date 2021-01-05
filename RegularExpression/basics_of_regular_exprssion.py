from re import *
#PREDEFINED CHARACTER SETS
pattern="[a-z]"
pattern1='[0-9]'
pattern2='[^0-9]'#except numbers (print values without numbers)
pattern3='[^a-z]'#(^) indicates the except lower case term
pattern4="[a-zA-Z]"#chk for both lower case and upper case
pattern5='[a-zA-Z0-9]'
pattern6='[^a-zA-Z0-9]'#shows only special character
#PREDEFINED CHARACTERS
pattern7="\s"#checking for spaces
pattern8="\S"#FOR except space we use capital letter
pattern9="\d"#check for digits
patern10="\D"#except digits
pattern11="\w"#except special charcter
pattern12="\W"#shows special character

mather=finditer(pattern12,"abc Z@7k")
for match in mather:
    print(match.start())#0 1 2 7
    print(match.group())#a b c k


#out=[(match.start(),match.group()) for match in mather]
#print(out)