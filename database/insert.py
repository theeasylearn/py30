import connection as con 
#create cursor 
mycursor = con.database.cursor()
sql = "insert into person (fullname,email,salary,mobile,weight,dob) values (%s,%s,%s,%s,%s,%s)"
fullname = input("Enter Full Name        : ")
email    = input("Enter Email            : ")
salary   = float(input("Enter Salary           : "))
mobile   = input("Enter Mobile Number    : ")
weight   = float(input("Enter Weight (in kg)   : "))
dob      = input("Enter Date of Birth (DD-MM-YYYY): ")
values = [fullname,email,salary,mobile,weight,dob]
#run sql query
mycursor.execute(sql,values)
con.database.commit()
print(mycursor.rowcount," rows inserted")
