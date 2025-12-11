#write code to connect with mysql 
import mysql.connector as mycon
import mysql
try:
    database = mycon.connect(host='localhost',user='root',passwd='',database='py30',port='3306')
    print('database connection created....')
except mycon.Errors as e:
    print('error in connection')
    print(e.errno)
    print(e.msg)

#create function to execute only insert,update,delete function
def run(sql,values,message):
    try:
        command = database.cursor() #create cursor
        command.execute(sql,values) 
        database.commit()
        print(message)
        key = input("press ENTER to continue....")
    except mysql.connector.errors.ProgrammingError as error:
        print("oops something went wrong, contact developer")
        print(error)
#create function to fetch data from table
def fetch(sql,values=None):
    try:
        mycursor = database.cursor(dictionary=True)
        if values == None:
            mycursor.execute(sql)   
        else:
            mycursor.execute(sql,values)   
        table = mycursor.fetchall() #return list of dictonary
        return table
    except mysql.connector.errors.ProgrammingError as error:
        print("oops something went wrong, contact developer")
        print(error)
        return None