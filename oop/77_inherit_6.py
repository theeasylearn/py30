class KB:
    def __init__(self,bytes):
        #create instance variable
        self.bytes = bytes
        print("KB class constructor called....")
    def getKB(self):
        #local variable
        result = self.bytes / 1024 
        return result
    
class MB(KB):
    def __init__(self, bytes):
        super().__init__(bytes) #calling parent class constuctor (required)
        print("MB class constructor called")
    def getMB(self):
        result = super().getKB()
        result = result / 1024 
        return result
    
bytes = int(input("Enter bytes"))
m1 = MB(bytes) #calling child class constructor
result = m1.getKB()
print(f" kilo bytes = {result}")
result = m1.getMB()
print(f" mega bytes = {result}")
