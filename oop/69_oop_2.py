#create class 
class Developer:
    #learn
    def learn(self):
        print("I can learn")
    #code
    def code(self):
        print("I can code")
    #debug
    def debug(self):
        print("I can debug")

#create object 
#object-name = classname()
mohit = Developer()
mohit.learn()
mohit.code()
mohit.debug()
print("_"*100)
ankit = Developer()
ankit.code()
ankit.debug()
ankit.learn()