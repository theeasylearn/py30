import connection as con 
sql = "select * from person order by id desc"
#create cursor 
mycursor = con.database.cursor(dictionary=True)
mycursor.execute(sql)
#single row fetch
# single = mycursor.fetchone()
#fetch all row 
table = mycursor.fetchall()
print(f"{'ID':<6} {'Full Name':<36} {'Salary':<10} {'Email':<32} {'Mobile'}")
print("-" * 102)  # Separator line (total width = 6+36+10+32+11 = 95 + spaces ≈ 102)
for row in table:
    output = f"{row['id']:<6} {row['fullname']:<36} {row['salary']:<10} {row['email']:<32} {row['mobile']}"
    print(output)