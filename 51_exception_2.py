#second example of exception handling mechanism 
#write a program to make sum of all values & find average in list 
# numbers = [None,'ankit']
numbers = [None,'ankit',10,20,30]
sum = 0
average = 0.0
count = 0
for num in numbers:
    try:
        sum = sum + num 
        count= count + 1
    except TypeError as e:
        print(f"{num} is invalid type of value, hense skipped")
try:
    average = sum/count
    print(f"sum = {sum} average = {average}")
except ZeroDivisionError:
    print('none of value are valid')