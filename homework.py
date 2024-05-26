#qustion1
#A

L1=['HTTP','HTTPS','FTP','DNS']
L2=[80,443,21,52]
d={key:value for key , value in zip(L1,L2)}
print(d)
______________________________________________
#B
num = int(input("enter a number to calculate it factorial: "))

if num < 0:
    print("factorial can't calculate for nigative number")
else:
  
    factorial = 1

    for i in range(1, number + 1):
        factorial = num * i
        
    print(f"factorial the num {num} is {factorial}")

_____________________________________________
#C
L=['Network','Bio','Programming','Physics','Music'] 

i = 0

for i in range(len(L)):
    if L[i].startswith("B"):
        print(L[i])
        
___________________________________________
#D
d= {a:a+1 for a in range(0,11)}
print(d)
_____________________________________________
#qustion2

binary_str = input("enter binary number to convert it : ")

try:
   
    decimal_number = int(binary_str, 2)
   
    print(f"the decimal number that equalvant to the binary {binary_str} is: {decimal_number}")
except ValueError:
   
    print("incorrect value .")
___________________________________________
#qustion3

import json
questions = { }
scores = 0
number=1
f = open("c:\questions.txt",'r')
questions = json.load(f)
f.close()
print("python quiz programm")
print("Enter t for True or f for False")
name = input("Enter your full name: ")
for ques in questions.keys():
    print("Question",number,": ", ques)
    ans = input("The answer is ")
    if ans.upper() == questions[ques].upper():
        scores = scores + 1
        print("Correct ")
    else:
        print ("Wrong")
    number = number + 1
result={name:scores}
m = open("score.txt",'w')
result = json.dump(result,m)
m.close()
_______________________________________________
#qustion4
class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"deposite: ${amount}. current balance : ${self.balance}.")
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"withdrawn: ${amount}. current balance: ${self.balance}.")
        else:
            print("the balance is insufficient for withdarawl !")

    def get_balance(self):
        return self.balance
    
account = BankAccount("123456789", "Suzan Shakohi")
account.deposit(1000)
account.withdraw(500)
print(f"current balance: ${account.get_balance()}.")


class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, interest_rate, balance=0.0):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)

    def __str__(self):
        return f"current balance: ${self.balance}. the interest rate: {self.interest_rate * 100}%."

savings_account = SavingsAccount("987654321", "Suzan Shakohi", interest_rate=0.02)
savings_account.deposit(1000)
savings_account.apply_interest()
print(savings_account)



