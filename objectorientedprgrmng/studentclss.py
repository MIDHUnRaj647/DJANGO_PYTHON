class Student:
    def stud_details(self,roll,name,course,total):
        self.roll=roll
        self.name=name
        self.course=course
        self.total=total
    def print_stud(self):
        print('roll=',self.roll)
        print('name=',self.name)
        print('course=',self.course)
        print('total=',self.total)
obj=Student()
# stud1=Student()
# stud1.stud_details('101','ajay','ece',150)
# stud1.print_stud()
#
# stud2=Student()
# stud2.stud_details('102','raju','eee',160)
# stud2.print_stud()
obj=Student() #
obj.name ='jinu'
obj.roll=103
obj.course='eee'
obj.total=150
obj.print_stud()
print(obj.total)