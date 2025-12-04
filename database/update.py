import connection as con 
sql = "update person set fullname=%s,email=%s,dob=%s,salary=%s,mobile=%s,weight=%s where id=%s"
id = int(input("Enter person id update"))
fullname = input("Enter Full Name        : ")
email    = input("Enter Email            : ")
salary   = float(input("Enter Salary           : "))
mobile   = input("Enter Mobile Number    : ")
weight   = float(input("Enter Weight (in kg)   : "))
dob      = input("Enter Date of Birth : ")
values = [fullname,email,dob,salary,mobile,weight,id]
#create cursor 
mycursor = con.database.cursor()
#run sql statement
mycursor.execute(sql,values)
con.database.commit()
print(mycursor.rowcount, ' rows updated...')