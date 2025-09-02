# write a program to display multiplication table of given number 
'''
    number 10

    10 x  1 = 10
    10 x  2 = 20
    10 x  3 = 30
    10 x  4 = 40
    10 x 10 = 100

'''
num = int(input("Enter number "))
for multiplier in range(1,11):
    result = num * multiplier
    print(f"{num} X {multiplier:2} = {result:3}")
    multiplier = multiplier + 1

