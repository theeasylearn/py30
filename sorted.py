lit=[4,7,3,8,2,1,0]
print(sorted(lit))
print(sorted(lit,reverse=True))



#o/p:[0, 1, 2, 3, 4, 7, 8]
#    [8, 7, 4, 3, 2, 1, 0]

days_in_month = {
    'jan': 1, 
    'feb': 8, 
    'mar': 3,
    'apr': 0, 
    'may': 5
}
print(sorted(days_in_month,key=lambda x:x[1]))

#['jan', 'mar', 'may', 'feb', 'apr']