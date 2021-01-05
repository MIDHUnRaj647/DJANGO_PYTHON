#find highest salary
from functools import *
class Emp:
    def __init__(self,eid,ename,desig,sal,exp):
        self.eid=eid
        self.name=ename
        self.desig=desig
        self.salary=sal
        self.exp=exp
    def __str__(self):
        return self.name + self.salary





#reading the file
f=open('employee','r')
employ=[]
for lines in f:
    eid,ename,desig,sal,exp=lines.rstrip("\n").split(",")
    employ.append(Emp(eid,ename,desig,sal,exp))
highest=reduce(lambda sal1,sal2:sal1 if sal1>sal2 else sal2, list(map(lambda emp:emp.salary,employ)))
print(highest)

#details of higest salary employ
employ=list(filter(lambda emp:emp.salary==highest,employ))
for emp in employ:
    print(emp)
#finding highest salary of developer designation
deve=list(filter(lambda emp:emp.desig=="devop",employ))
devsala=list(map(lambda emp:emp.salary,deve))
devhigh=reduce(lambda sal1,sal2:sal1 if sal1>sal2 else sal2,devsala)
#devsal=reduce(lambda sal1,sal2:sal1 if sal1>sal2 else sal2,employ),list(map(lambda emp:emp.salary,employ)),list(filter(lambda desig:desig=="devop",employ))
#print(employ)
print(devhigh)