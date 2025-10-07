import datetime

# date1=input("Enter date of birth(p1):")
# date2=input("Enter date of birth(p2):")

# parsedate1=datetime.date.fromisoformat(date1)
# parsedate2=datetime.date.fromisoformat(date2)

# if parsedate1>parsedate2 :
#     print("person1 is younger")
# elif parsedate2>parsedate1:
#     print("person2 is younger")
# else:
#     print("Both are of same age!")

'''o/p:Enter date of birth(p1):2025-12-13
Enter date of birth(p2):2024-08-05 
person1 is younger'''

#timedelta example:

period1=datetime.timedelta(650,12)
period2=datetime.timedelta(320,10)
gapday=period1-period2
print(gapday)

#timestamp example:
date1=datetime.datetime(2025,12,13)
date2=datetime.datetime(2021,1,13)
sec1=date1.timestamp()
sec2=date2.timestamp()
conv1=sec1/(24*3600)
conv2=sec2/(24*3600)
print(conv1-conv2)