employees={101:{'empid':101,'name':'raju','designation':'mech','salary':15000},102:{'empid':102,'name':'ramu','designation':'mech','salary':25000},103:{'empid':103,'name':'riju','designation':'ec','salary':35000},104:{'empid':104,'name':'roju','designation':'eee','salary':10000}}
count=1
for i in employees:
    # print(employees[i]['name'])
    if 'experience' not in employees:
        print('enter the experience of',count,'th employee')
        n = int(input('enter here'))
        employees[i]['experience']=n
        print(employees[i])
        i+=1
        count+=1