'''
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
* 
'''

for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=' ')
    print()
for i in range(5,1,-1):
    for j in range(1,i):
        print("*",end=' ')
    print()
print()
'''
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1 
'''
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end=' ')
    print()
for i in range(5,1,-1):
    for j in range(1,i):
        print(i-1,end=' ')
    print()
print()
'''
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1
'''
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=' ')
    print()
for i in range(5,1,-1):
    for j in range(1,i):
        print(j,end=' ')
    print()