# numbers # strings # booleans # ***** # Lists # Dictionaries
# class Point:
#     def move(self):
#         print("Move")
#
#     def draw(self):
#         print("draw")
#
#
# point1 = Point()
# point1.x = 10
# point1.y = 20
# print(point1.x)
# point1.draw()
#
# point2 = Point()
# point2.x = 2
# print(point2.x)

## Introduce constroctor which get's called while creating the object
# class Point:
#     def __init__(self, x, y):  # constructor method
#         self.x = x
#         self.y = y
#     def move(self):
#         print("Move")
#
#     def draw(self):
#         print("draw")
#
# point = Point(10, 20)
# point.x = 13
# print(point.x)
# Exercise -
class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f'Hi, I am {self.name}')

aradhana = Person(" Aradhana Singh")
# print(aradhana.name)
aradhana.talk()

bob = Person( "Bob Smith")
bob.talk()
