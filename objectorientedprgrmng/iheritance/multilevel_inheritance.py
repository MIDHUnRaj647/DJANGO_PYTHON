class Parent:
    def m1(self):
        print('inside the parent')
class Child(Parent):
    def m2(self):
        print('inside child')

class SubChild(Child):
    def m3(self):
        print('inside sub child')

# sb=SubChild()
# sb.m3()
sb=SubChild()
sb.m1()

ch=Child()
#ch.m3()    cannot use this, parent cannot acces subchild
ch.m1()
ch.m2()


p=Parent()
#p.m3()    cannot use this, parent cannot acces subchild
#p.m2()    cannot use this, parent cannot acces subchild
p.m1()