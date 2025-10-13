#write a program to generate exception as per business rule 
#accept user's age and calculate remaining year in job. if age is above 60 and less then 18, raise custom exception 

while True:
    try:
        age = int(input("Enter your age")) 
        if age<18 or age>60:
            raise ValueError #this will execute except block with ValueError
        else:
            remaining_job_year = 60 - age 
            print(f"you have {remaining_job_year} year left for job ")
    except ValueError as e:
        if  len(e.args) == 0:
            print("unusal age for job age must be between 18 to 60 (both including)")
        else:
            print('not a valid age (age must be number)')
    else:
        break #stop loop 
    finally:
        print ("Thank your for using program")    