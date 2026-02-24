class Person:
    def __init__(self, name, age):
        self.name= name
        self.age= age
   
    def introduce(self):
        print(f"Hello, My name is {self.name} and I'm {self.age} years old.")

class Nepali:
    def __init__(self, name, age):
        self.name= name
        self.age= age
   
    def introduce(self):
        print(f"Namaste, Mero naam {self.name} ho ra ma {self.age} barsa ko chu.")

class Student(Person, Nepali):

    def __init__(self, name, age, gender):
        super().__init__(name, age)
        self.gender = gender
    
    def introduce(self):
        Person.introduce(self)
        Nepali.introduce(self)
        print(f"Hello, My name is {self.name}, I'm {self.age} years old, and I'm {self.gender}.")
    

p1=Person("Aayush", 21)
p1.introduce()

s1=Student("Ace", 21, "Male")
s1.introduce()

print(Student.mro())