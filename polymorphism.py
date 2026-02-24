# class Animal:
#     def speak(self):
#         print("Animal speaks")
# class Dog(Animal):
#     def speak(self):
#         print("Dog barks")
    
# class Cat(Animal):
#     def speak(self):
#         print("Cat meows")
    
# animals = [Dog(), Cat()]
# for animal in animals:
#     animal.speak()

# def add(x, y, z=0):
#     return x + y + z

# print(add(2,3))
# print(add(2,3,4))


# def add (a, *b):
#     for n in b:
#         a += n
#     return a

# print(add(7))
# print(add(7, 3,4,5,6,8,9,10))




# def add (*b):
#     a = ""
#     for n in b:
#         if isinstance(n, int):
#              a=0
#         a += n
#     return a

# print(add())
# print(add(3,4,5,6,8,9,10))
# print(add("h", 'ello'))


def add(**kwargs):
    print(kwargs)
    n=True
    if isinstance(n, int):
        print("N is Integer")


add(a=1, b=2, c=3, d=43, e=54, f=65, g=76, h=87, i=98, j=109)
add(x="h", y='ello')