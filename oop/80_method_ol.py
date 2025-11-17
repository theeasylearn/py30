class compute:
    def area(self,x=None,y=None):
        if x!=None and y!=None:
            return x*y
        elif x!=None:
            return x*x
        else:
            return 0
        
c1=compute()
print(c1.area())
print(c1.area(3))
print(c1.area(3,5))