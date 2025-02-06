# class Bank:
#     def __init__(self, first_name, last_name, age, balance=0):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.balance = balance
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#         else:
#             print("Invalid amount!")
#
#     def withdraw(self, amount):
#         if 0 < amount <= self.balance:
#             self.balance -= amount
#         else:
#             print("Invalid amount!")
#
#     def info(self):
#         print(f"Name: {self.first_name}")
#         print(f"Surname: {self.last_name}")
#         print(f"Age: {self.age}")
#         print('#' * 20)
#
#     def get_balance(self):
#         print(f"{self.first_name}'s balance: {self.balance}")
#
#
# bank_1 = Bank("Arsen", "Kenzhegulov", 22)
# bank_2 = Bank("Nurbol", "Kadyrbekov", 17)
# bank_3 = Bank("Emir", "Kachkynov", 13)
# bank_4 = Bank("Asylbek", "Arstanbekov", 14)
# bank_5 = Bank("Ainagul", "Azhybaeva", 38)
# bank_6 = Bank("Elnara", "Kasymbekova", 15)
# bank_7 = Bank("mirzhana", "Begalieva", 15)
#
# users = [bank_1, bank_2, bank_3, bank_4, bank_5, bank_6, bank_7]
#
# while True:
#     print("1. Users")
#     print("2. Choice user")
#     print("3. Exit")
#     choice = int(input("Enter your choice(1,2,3): "))
#     if choice == 1:
#         for i in range(len(users)): # 0 1 2 3 4 5 6
#             print(f'{i}. {users[i].first_name} {users[i].last_name}')
#     elif choice == 2:
#         user_number = int(input("Enter the user number: "))
#
#         if 0 <= user_number < len(users):
#             user = users[user_number]
#             while True:
#                 user.info()
#
#                 print("1. Deposit")
#                 print("2. Withdraw")
#                 print("3. Balance")
#                 print("4. Back")
#                 choice = int(input("Enter your choice(1,2,3,4): "))
#
#                 if choice == 1:
#                     amount = int(input("Enter the amount: "))
#                     user.deposit(amount)
#                 elif choice == 2:
#                     amount = int(input("Enter the amount: "))
#                     user.withdraw(amount)
#                 elif choice == 3:
#                     user.get_balance()
#                 elif choice == 4:
#                     break
#                 else:
#                     print("Invalid choice!")
#             else:
#                 print("Invalid user number!")
#     else:
#         break

