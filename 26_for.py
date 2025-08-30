'''(start,end)
i=(1,6),j=(1,2) *
i=(2,6),j=(1,3) * *
i=(3,6),j=(1,4) * * *
i=(4,6),j=(1,5) * * * *
i=(5,6),j=(1,6) * * * * *
i=(6,6) # loop  did not run due to start=stop
'''

'''
*
* *
* * *
* * * *
* * * * *
'''

# only valid for * not for number
for i in range(0,5):
    for j in range(0,i+1):
        print("*",end=' ')
    print()


'''
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
'''

for i in range(1,6):
    for j in range(1,i+1):
        print(i,end=' ')
    print()

'''
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
'''

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=' ')
    print()