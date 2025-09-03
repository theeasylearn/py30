# example of user defined function 
def getMinutes(hours,minutes):
    total_minutes = hours * 60
    total_minutes += minutes
    hours = 0 
    minutes = 0 
    return total_minutes


hours = int(input("Enter hours"))
minutes = int(input("Enter minutes"))

#call function 
total_minutes = getMinutes(hours,minutes)
print(f"total minutes = {total_minutes}")
