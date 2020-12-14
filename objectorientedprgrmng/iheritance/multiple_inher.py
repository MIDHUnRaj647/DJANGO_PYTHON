class Parent:
    def m1(self):
        print('inside the parent')
class Child():
    def m2(self):
        print('inside child')

class SubChild(Child,Parent): #herer sub child only required parent, child does not need parent. here both are satisfied
    def m3(self):
        print('inside sub child')
