#filter(lamda x:condition(return:ture/false),iterable)

#print even numbers

lit=[1,2,3,4,5,6,7,8,9,10]

res=filter(lambda x:x%2==0,lit)
print(list(res))

#o/p:[2, 4, 6, 8, 10]

#filter months according to no. of days
days_in_month = {
    'jan': 31, 
    'feb': 28, 
    'mar': 31,
    'apr': 30, 
    'may': 31
}

res1=filter(lambda x:days_in_month[x]==31,days_in_month)
print(list(res1))

#['jan', 'mar', 'may']