#write code to connect with mysql 
import mysql.connector as mycon
try:
    database = mycon.connect(host='localhost',user='root',passwd='',database='py30',port='3306')
    print('database connection created....')
except mycon.Errors as e:
    print('error in connection')
    print(e.errno)
    print(e.msg)

#create function 
def run(sql,values,message):
    #create cursor
    mycursor = database.cursor()
    #run sql command 
    mycursor.execute(sql,values)
    database.commit()
    print(message)