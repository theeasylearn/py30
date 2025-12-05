#write code to connect with mysql 
import mysql.connector as mycon
try:
    database = mycon.connect(host='localhost',user='root',passwd='',database='py30',port='3306')
    print('database connection created....')
except mycon.Errors as e:
    print('error in connection')
    print(e.errno)
    print(e.msg)