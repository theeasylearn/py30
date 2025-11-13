# hybrid inheritance
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

class Doctor(Student):
    def diagnosis(self):
        print("I can diagnosize patient")
    def treatment(self):
        print("I can give treatment")
    def whatICanDo(self):
        super().whatICanDo()
        self.diagnosis()
        self.treatment()
class Developer(Student):
    def code(self):
        print("I can write code")
    def debug(self):
        print("I can debug code")
    def whatICanDo(self):
        super().whatICanDo()
        self.code()
        self.debug()


#create object student class
d2 = Doctor()
d2.whatICanDo()

d1 = Developer()
d1.whatICanDo()