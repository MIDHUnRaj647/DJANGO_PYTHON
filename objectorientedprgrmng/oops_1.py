class person:
    def person_1(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender


    def printperson(self):
        print('name',self.name)
        print('age',self.age)
        print('gender',self.gender)


obj=person()
obj.person_1('ajay',24,'male')
obj.printperson()

obj1=person()
obj1.person_1('raju',34,'male')
obj1.printperson()