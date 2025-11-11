#create class 
class Student:
    #create class variable
    college = "ABC"
    #create constructor
    def __init__(self,name,surname,rollno):
        #create instance variable 
        self.name = name 
        self.surname = surname 
        self.rollno = rollno
    def display(self):
        print(f"Surname ",self.surname," name ",self.name," rollno ",self.rollno)
    
#create object
#object = classname()
m1 = Student("mohit","sukheja",'1001') #run __init__ method automatically (constructor)
m1.display()
print("College name ",m1.college)

name = input("Enter name")
surname = input("Enter surname")
rollno = input("Enter roll no")

m2 = Student(name,surname,rollno)
m2.display()
print("College name ",m2.college)
#change class variable value using classname
Student.college = "SunRise college"
print("College Name ",Student.college)
print("College Name using m1",m1.college)
print("College Name using m2",m2.college)
print("name using m1",m1.name)
print("name using m2",m2.name)