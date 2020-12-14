students={101:{'roll':101,'name':'vijay','total':140,'course':'bca'},102:{'roll':102,'name':'ajay','total':150,'course':'bca'},}


def printstudent(**args):
    id=args.get('roll')
    if id in students:
        # if "prop" in args:
            propp=args.get('prop')
            if propp in students[id]:

                print(students[id][propp])
                print(students[id]['name'])
    else:
        print('student not found')

printstudent(roll=101,prop='total')
