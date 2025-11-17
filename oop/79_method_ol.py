class humman:
    def sayHello(self,name=None):
        if name!=None:
            print("Hello"+name)
        else:
            print("hello")

h1=humman()
h1.sayHello()
h1.sayHello("The Easy Learn Academy")