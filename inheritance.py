# Inheritance- Machanisam to reuse the code- in programming we should not define something twice
## Because- to avoid below 2 class for same purpose - walk
# class Dog:
#     def walk(self):
#         print("walk")
#
#
# class Cat:
#     def walk(self):
#         print("walk")
class Mammal:
    def walk(self):
        print("walk")

class Dog(Mammal):  # but python doesn't like empty class so add pass
     def bark(self):
         print("bark")

class Cat(Mammal):
    pass

dog1= Dog()
dog1.walk()
dog1.bark()