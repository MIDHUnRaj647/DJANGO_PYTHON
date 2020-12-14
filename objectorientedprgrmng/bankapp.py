class Bank:
    bank_name="sbt"
    def acc_details(self,acc_no,name,mini_bal):
        self.acc_no=acc_no
        self.name=name
        self.minbal=mini_bal

    def deposit(self,amount):
        self.minbal+=amount
        print('Your account no of',self.acc_no,'is being credited with ',amount,'Rs, Current balance is ',self.minbal)
    def withdraw(self,debit):
        if self.minbal<debit:
            print('your account does not have sufficient balane')
        else:
            self.minbal-=debit
            print('your account',self.acc_no, 'has been debited of rs',debit,'your current balance is',self.minbal)
    def bal_check(self):
        print('your balance amount is',self.minbal)



obj=Bank()
obj.acc_details(121,'raju',53000)
obj.withdraw(5000)
obj.bal_check()
obj.acc_details(123,'riju',65655)
obj.withdraw(65655)
obj.withdraw(1)

