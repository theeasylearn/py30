# multiple inheritance
class Animal:
    def eat(self):
        print("Animal can eat")
    def sleep(self):
        print("Animal can sleep")
class Human:
    def talk(self):
        print("Human can talk")
    def think(self):
        print("Human can think")

class Student(Animal,Human):
    def read(self):
        print("I can read")
    def write(self):
        print("I can write")
    def whatICanDo(self):
        # super().eat()
        # super().sleep()
        # super().talk()
        # super().think()
        self.eat()
        self.sleep()
        self.think()
        self.talk()
        self.read()
        self.write()


#create object student class
s1 = Student()
s1.whatICanDo()