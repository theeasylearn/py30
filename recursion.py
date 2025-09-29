#Recursion:

#Example1:

def counter(n):
    if n==0:
        print("stop")
    else:
        print(n)
        counter(n-1)

counter(5)

#Example2:

def factorial(num):
    
    if num==1:
        return 1
    else:
        return num*factorial(num-1)
        
        
ans=factorial(5)
print(ans)
    