from re import *
f=open("REG_NO_LIST",'r')
fout=open('validreg','w')
fout1=open('invalidreg','w')

regnum=set()
for num in f:
    regnum.add(num.rstrip('\n'))
#print(regnum)
rule='KL\d{2}[A-Z]{1,2}\d{1,4}'#{MIN NO,MAX NO}
for vehno in regnum:

#vehiclenum=input('enter the reg no')
    matcher=fullmatch(rule,vehno)
    if matcher!=None:
       fout.write((vehno+'\n'))

    else:
        fout1.write((vehno+'\n'))
