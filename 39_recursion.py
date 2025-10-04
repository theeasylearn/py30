# concept of recursion 
# write a program to findout factorial of given number 
#  input 5 : 1 x 2 x 3 x 4 x 5 = 120
def getFactorial(number,multiplier):
    if multiplier<number:
        multiplier  = multiplier + 1  #3
        return multiplier * d(number,multiplier) #5 5
    return 1
number = int(input("Enter number to get factorial"))
multiplier = 1
# while multiplier<=number:
#     factorial = factorial * multiplier # 1
#     multiplier  = multiplier + 1 #2 
factorial = getFactorial(number,multiplier)
print(factorial)
