#write a program to accept appointment date from user and check appointment date must be of future else raise valueerror
from datetime import datetime as dt
try:
    user_given_date = input("Enter your appointment date must be of future (dd-mm-yyyy)")
    print(user_given_date) 
    appointment_date = dt.strptime(user_given_date,"%d-%m-%Y")
    if appointment_date<dt.today():
        raise ValueError("appointment date must be future date only")    
except ValueError as e:
    if e.args[0].find('appointment')<0:
        print("invalid date")
    else:
        print(e)
else:
    print("your appointment has been booked successfully")
finally:
    print("thank you for using our appointment booking program")

