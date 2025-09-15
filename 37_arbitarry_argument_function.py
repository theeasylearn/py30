#arbitary argument function
def getSumAverage(*numbers):
    #10,20,30...50
    sum = 0 
    for num in numbers: 
        sum = sum + num
    average = sum / len(numbers)
    return sum,average #it returns multiple values

result = getSumAverage(10,20,30,40,50)
print(result)
result = getSumAverage(100,200,300)
print(result)
result = getSumAverage(100,2000)
print(result)

