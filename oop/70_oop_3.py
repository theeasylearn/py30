#create class 
class Developer:
    #create instance variable (variable declared inside class)
    def __init__(self,language):
        self.langugage = language
    #learn
    def learn(self):
        #you can access instance variable only using self
        print("I can learn " ,self.langugage)
    #code
    def code(self):
        print("I can code ",self.langugage)
    #debug
    def debug(self):
        print("I can debug ",self.langugage)

#create object 
#object-name = classname()
mohit = Developer('Python')
mohit.learn()
mohit.code()
mohit.debug()
print("_"*100)
ankit = Developer('C')
ankit.code()
ankit.debug()
ankit.learn()