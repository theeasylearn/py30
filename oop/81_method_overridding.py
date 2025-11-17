#example of method overidding
from playsound import playsound
class Animal:
    def sound(self):
        print("i can make some sound")
        playsound('../sound/animal.wav')
class Cat(Animal):
    #method overidding
    def sound(self):
        print("cat can mew mew")
        playsound('../sound/cat.wav')
class Dog(Animal):
    #method overidding
    def sound(self):
        print("dog can bhaw bhaw")
        playsound('../sound/dog.wav')
a1 = Animal()
c1 = Cat()
d1 = Dog()

a1.sound()
c1.sound()
d1.sound()

