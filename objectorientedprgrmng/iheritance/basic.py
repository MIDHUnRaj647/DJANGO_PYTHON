#inheritance

#acquiring properties of parent class to basic class
#base-derived, parent-child, superclass-sub class


class Parent:
    def phone(self):
        print('have nokia 5310')
        print('this is my only phone')

    def __laptop(self):#this is a private func thus the child cannot acces it
        print('i have a laptop')

class Child(Parent):
    def bike(self):
        print('i have a bike')
    def change_num(self,num):
        self.change_number=num
        print(num)

ch=Child()
ch.change_num(245)
ch.change_number
