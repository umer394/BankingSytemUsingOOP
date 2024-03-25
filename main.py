# Banking System using OOP
#Parent Class : User
#Has a function to show user details
#Child Class :Bank
#Stores details about the account balance
#Stores details about the amount
#Allow for deposit,withdraws,view_balance

class User:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_user_details(self):
        print("Personal Details")
        print("")
        print("Name: ",self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)

class Bank(User):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balance = 0

    def deposit(self,amount):
        self.amount = amount
        self.balance = self.balance + amount
        print("Account balance has been updated : $", self.balance)
        print("You deposit $",self.amount , "in Your Bank Account" )

    def withdraw(self,amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insuficient Funds! Balance Available: ", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Account balance has been updated : $", self.balance)
            print("You withdraw $",self.amount)

    def view_balance(self):
        self.show_user_details()
        print("Your Account Current balance : $", self.balance)

Umer = Bank("ali",30,"male")
Umer.deposit(1000)
print("\n")
Umer.withdraw(400)
print("\n")
Umer.withdraw(450)
print("\n")
Umer.view_balance()
