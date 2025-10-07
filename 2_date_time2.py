import datetime 

def getDate():
    year=int(input("Enter the year(yyyy): "))
    month=int(input("Enter the month(mm): "))
    date=int(input("Enter the date(dd): "))
    
    actual_date=datetime.date(year,month,date)
    print(actual_date)

d=getDate()

# o/p:
# Enter the year(yyyy): 2012
# Enter the month(mm): 12
# Enter the date(dd): 5
# 2012-12-05

def getparsedate():
    
    date=input("Enter the date(yyyy-mm-dd): ")
    
    parsedate=datetime.date.fromisoformat(date)
    print(parsedate)
    
d1=getparsedate()

# o/p:
# Enter the date(yyyy-mm-dd): 2012-12-30
# 2012-12-30