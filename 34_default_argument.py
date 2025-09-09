# example of default argument 
def toinch(meter,foot=0,inches=0):
    #calculate and return total inches
    temp1 = (foot * 12) + inches
    temp2 = (meter * 3.281 * 12)
    result = temp1 + temp2
    return result

result = toinch(1,1,5)
print(result)

result2 = toinch(2,2)
print(result2)

result3 = toinch(3)
print(result3)