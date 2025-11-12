#example of multi-level inheritance 
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
class Developer(Student):
    def code(self):
        print("I can write code")
    def debug(self):
        print("I can debug code")
    def whatICanDo(self):
        #Method Overridding
            # when we create same method(method with same name and same no of arguments) in parent and child class, it is called Method Overridding
        super().whatICanDo()
        self.code()
        self.debug()

d1 = Developer()
d1.whatICanDo()