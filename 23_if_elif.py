# payment Gateway 
age = int(input("enter your age"))
balance = 50000
if age<18:
    print("you are not valid to do transaction")
else:
    amount = int(input("enter amount you have to withdraw"))
    if balance < amount:
        print("your balance is insufficient")
    elif balance == amount:
        print("transaction is successful")
        balance -=amount
        print(f"your balance is {balance} you need to deposit minimum amount")
    else:
        print("transaction is successful")
        balance -=amount
        print(f"your balance is {balance}")     
