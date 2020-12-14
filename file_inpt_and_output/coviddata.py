f=open("covid_19_india (1).csv")
dict={}
for lines in f:
    data=lines.rstrip('\n').split(',')
    state=data[3]
    #if state=='Telengana':
        #state='Telangana'
    cured=data[6]
    death=data[7]
    confirmed=data[8]
    if state not in dict:
        dict[state]={'state':state,'confirmed':confirmed,'cured':cured,'death':death}
    else:
        dict[state]={'state':state,'confirmed':confirmed,'cured':cured,'death':death}

def printcvddata(**args):
    staate=args.get('state')
    if staate in dict:
        print(staate, dict[staate]["confirmed"])
        if "property" in args:
            prop=args['property']
            if prop in dict[staate]:
                print(prop,'>>', dict[staate][prop])
    else:
                print('state not found')


printcvddata(state='Haryana',property='cured')



