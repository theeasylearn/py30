import datetime

birthd1=datetime.date(2025,12,13)
birthd2=datetime.date(2023,4,23)
print(birthd1>birthd2)
#True

btime1=datetime.datetime(2011,3,12,5,12,0)
btime2=datetime.datetime(2023,2,15,7,45,0)
print(btime2-btime1)
#4358 days, 2:33:00

period1=datetime.timedelta(650,12)
period2=datetime.timedelta(320,10)
gapday=period1-period2
print(gapday)
#330 days, 0:00:02

today=datetime.date.today()
print(today)
#2025-10-03

now=datetime.datetime.now()
print(now)
#2025-10-03 10:21:22.733255

#Indian format
format=now.strftime("%a - %d/%m/%y %H:%M:%S")
print(format)
#Fri - 03/10/25 10:33:41

#Us format
usf=now.strftime("%a-%m-%d-%y %H:%M:%S")
print(usf)
#Fri-10-03-25 10:36:23