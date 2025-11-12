#example of single level inheritance 
#parent/super/base class
class Person:
    def walk(self):
        print("I can walk")
    def talk(self):
        print("I can talk")
    def sleep(self):
        print("I can sleep")

#inherit Person class into Student class
#child/derived/sub class
class Student(Person):
    def read(self):
        print("I can read")
    def write(self):
        print("I can write")
    def whatICanDo(self):
        #calling parent class method
        super().walk()
        super().talk()
        super().sleep()
        #calling same class method
        self.read()
        self.write()

#create parent class object
p1 = Person()
p1.walk()
p1.talk()
p1.sleep()


#create child class object
s1 = Student()
#we can call parent class methods using child class object
s1.walk()
s1.talk()
s1.sleep()
s1.read()
s1.write()
s1.whatICanDo()