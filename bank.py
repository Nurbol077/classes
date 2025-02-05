class Bank:
    def __init__(self,first_name, last_name, age, balance=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.balance = balance


    def deposit(self,amount):
        if amount>0:
            self.balance += amount

    def withdraw(self,amount):
        if 0 < amount <= self.balance:
            self.balance -= amount

    def info(self):
        print(f'Name; {self.first_name}')
        print(f'Surname; {self.last_name}')
        print(f'Age; {self.age}')
        print('#' * 20)

    def get_balance(self):
        print(f"{self.first_name}'s balance: {self.balance}")

bank_1 = Bank("Arsen", "Kenzhegulov", 22)
bank_2 = Bank("Nurbol", "Kadyrbekov", 17)
bank_3 = Bank("Emir", "Kachkynov", 13)
bank_4 = Bank("Asylbek", "Arstanbekov", 14)
bank_5 = Bank("Ainagul", "Azhybaeva", 38)
bank_6 = Bank("Elnara", "Kasymbekova", 15)
bank_7 = Bank("mirzhana", "Begalieva", 15)


while True:
    print("1. Deposit ")
    print("2. Withdraw ")
    print("3. Info ")
    print("4. Balance ")
    print("5. Exit ")
    choice = int(input("; "))

    if choice==1:
        amount = int(input(": "))
        bank_1.deposit(amount)
    elif choice == 2:
        amount = int(input(": "))
        bank_1.withdraw(amount)
    elif choice == 3:
        bank_1.info()
    elif choice ==4:
        bank_1.get_balance()
    elif choice == 5:
        break
    else:
        print("Invalid choice")

