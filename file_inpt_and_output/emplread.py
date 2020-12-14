f=open("employee")
emp_dict={}
for lines in f:
    id,name,desig,exp,salary=lines.rstrip('\n').split(',')

    if id not in emp_dict:
        emp_dict[id]={'id':id,'name':name,'desig':desig,'exp':exp,'salary':salary}
    print(emp_dict)