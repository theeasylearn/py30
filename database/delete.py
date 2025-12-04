import connection as con 
sql = "delete from person where id = %s"
id = int(input("Enter person id to delete"))
values = [id]
#create cursor 
mycursor = con.database.cursor() 
#run sql command
mycursor.execute(sql,values)
con.database.commit() #required 
print(mycursor.rowcount, ' rows deleted')
