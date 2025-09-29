# #example1:

# amount=2000
# def func():
#     #global VarName
#     global amount
    
#     amount=1000
#     amount=amount+5
#     print(amount)  
# print(amount)
# #2000
# func()
# #1005
# print(amount)
# #2000

#example2:

bank_balance=50000
transactionNo=0

def deposite():
    global bank_balance,transactionNo
    
    amount=int(input("Enter the number to deposite money: "))
    bank_balance=bank_balance+amount
    transactionNo=transactionNo+1
    print("Your ammount is deposite successfully!")
    
def withdraw():
    global bank_balance,transactionNo
    
    amount=int(input("Enter the number to withdraw money: "))
    bank_balance=bank_balance-amount
    transactionNo=transactionNo+1
    print("Your ammount is withdraw successfully!")
    
def passbook():
    print("----------Your PassBook----------")
    print("Total Transactions: ",transactionNo)
    print("Bank balance: ",bank_balance)
    
deposite()
print("-----------------------------------------------------------------")
withdraw()
print("-----------------------------------------------------------------")
passbook()
print("-----------------------------------------------------------------")

#o/p:
# Enter the number to deposite money: 500
# Your ammount is deposite successfully!
# -----------------------------------------------------------------
# Enter the number to withdraw money: 200
# Your ammount is withdraw successfully!
# -----------------------------------------------------------------
# ----------Your PassBook----------
# Total Transactions:  2
# Bank balance:  50300
# -----------------------------------------------------------------