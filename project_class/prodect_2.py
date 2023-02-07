# exercise deposite and withdraw
class Account:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
    def __str__(self):
        return f"Account owner: {self.owner}\nAccount balance: ${self.balance}"

    def deposit(self, a):
        self.balance += a
        print('Deposit Accepted')

    def withdraw(self, b):
        if self.balance >= b:
            self.balance -= b
            print('Withdrawal Accepted')
        else:
            print('Funds Unavailable!')

print("Hello, Halyk Bank")
a = input("Choose the owner: ")
print(f"what do you want {a} :")
print("If you want to deposit money: input DEP")
print("If you want to withdraw money: input WITH")
s = input()

deposit = Account(a, 400)
if s == "DEP":
    n = int(input())
    deposit = Account(a, n)
    print(deposit)
elif s == "WITH":
    n = int(input())
    deposit.withdraw(n)








