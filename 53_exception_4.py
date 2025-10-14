#convert user given date into date object
from datetime import datetime 
while True:
    try:
        user_given_date = input("Enter your birth date (dd-mm-yyyy)")
        print(user_given_date) 
        #let us convert user given date into date object 
        birth_date = datetime.strptime(user_given_date,"%d-%m-%Y") 
        print(datetime.strftime(birth_date,"%A %d-%m-%Y"))
        break
    except ValueError as e:
        print("invalid date, date must be practically valid")

print("Good bye")