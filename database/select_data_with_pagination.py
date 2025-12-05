import connection as con 
mycursor = con.database.cursor(dictionary=True)
start = 0
while True:
    sql = "select * from person order by id desc limit %s,10"
    #create cursor 
    values = [start]
    mycursor.execute(sql,values)
    #fetch all row 
    table = mycursor.fetchall()
    if len(table) == 0:
        break #while loop break
    print(f"{'ID':<6} {'Full Name':<36} {'Salary':<10} {'Email':<32} {'Mobile'}")
    print("-" * 102)  # Separator line (total width = 6+36+10+32+11 = 95 + spaces ≈ 102)
    for row in table:
        output = f"{row['id']:<6} {row['fullname']:<36} {row['salary']:<10} {row['email']:<32} {row['mobile']}"
        print(output)
    key = input("press enter to continue")
    start = start + 10