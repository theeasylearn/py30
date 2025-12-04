#write code to connect with mysql 
import mysql.connector as connector 
try:
    database = connector.connect(host='localhost',user='root',passwd='',database='py30',port='3306')
    print('database connection created....')
except connector.Errors as e:
    print('error in connection')
    print(e.errno)
    print(e.msg)


