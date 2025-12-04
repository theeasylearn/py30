import connection as con 
sql = "select * from person order by id desc"
#create cursor 
mycursor = con.database.cursor(dictionary=True)
mycursor.execute(sql)
#single row fetch
single = mycursor.fetchone()
print(single)