#Create class Product store name,price,stock as instance variable using constructor. also add method display which will show name, price and stock. also add method printValue which will display total value of product  
#create class 
class Product:
    #create constuctor
    def __init__(self,name,price,stock):
        #create instance variable
        self.name  = name
        self.price = price  
        self.stock = stock 
        print("constructor called....")
    def display(self):
        #accessing instance variable use self. (required)
        print("Name ",self.name)
        print("Price = ",self.price)
        print("Stock = ",self.stock)
        print("_"*100)
    def printValue(self):
        self.display() #call same class function
        print("Total value = ",self.price * self.stock)
    
#create object (class type variable is called object)
#object-variable = classname()
p1 = Product('IPhone 17 pro max',99000,2) #this will call constructor automatically
p1.display()
p1.printValue()

#create another object
p2 = Product("Macbook air ",85000,10) 
p2.display()
p2.printValue()
