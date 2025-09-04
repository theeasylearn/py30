# 1	 Without return value without argument
def printLine():
    print("_"*100)
    return None

# 2	Without return value with argument 
def printLetter(letter,howManyTimes):
    print(letter*howManyTimes)
    return None 
# 3	 With return value without argument
def getPi():
    # local variable
    pi = 3.141516
    return pi 
# 4	With return value with argument 
def toCelicius(fahrenheit):
    #local variable
    ceilcius = (fahrenheit - 32) * (5/9)
    return ceilcius

printLine() #call
printLetter('~',100)
print("The easylearn academy")
printLetter('!',80)
printLine()
pi = getPi()
print(f"value of pi = {pi}")
print(pi)
fahrenheit = float(input("Enter fahrenheit"));
ceilcius = toCelicius(fahrenheit)
print(f"Ceilcius = {ceilcius}")