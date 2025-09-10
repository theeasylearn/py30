# function that return multiple value 
def getResult(num1,num2):
    #addition subtraction multiplication division
    # local variable (variable created inside function are local variables. such variables are available inside function in which it is created)
    add = num1 + num2 
    sub = num1 - num2
    mul = num1 * num2 
    div = num1 / num2 
    return add, sub, mul, div 

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
result = getResult(num1,num2)
print(result)
