# convert string into date 
import datetime as dt 
husband_birth_date = input("Enter husband birth date (dd-mm-yyyy)")
husband_date = dt.datetime.strptime(husband_birth_date,"%d-%m-%Y")
print(husband_birth_date)


wife_birth_date = input("Enter wife birth date (dd-mm-yyyy)")
wife_date = dt.datetime.strptime(wife_birth_date,"%d-%m-%Y")
print(wife_birth_date)

#findout who is elder
if husband_date>wife_date:
    print("wife is elder then husband")
else:
    print("husband is elder then wife")

