import datetime as dt 
#current date & time
print(dt.datetime.now())

#current date 
print(dt.date.today())

#indian format 
indian_format_date = dt.datetime.now().strftime("%d-%m-%Y")
print(indian_format_date)

#us format date 
us_format_date = dt.datetime.now().strftime("%m-%d-%Y")
print(us_format_date)

#indian format 
indian_format_date_time = dt.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
print(indian_format_date_time)


