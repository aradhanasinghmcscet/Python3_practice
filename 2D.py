# REcatangular array
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# # matrix[0][1] = 20
# # print(matrix[0][1])
# for row in matrix:
#     for item in row:
#         print(item)
# numbers = [2, 5, 4, 7, 5, 9]
# # numbers.insert(0,10) # add item
# numbers.remove(2)  # Remove index clear()
# numbers.pop(1)
# numbers.sort()
# numbers.reverse()
# print(50 in numbers)
# print(numbers.count(5))
# numbers2 = numbers.copy()
# numbers.append(19)
# print(numbers)
# print(numbers2)
# remove duplicates
# numbers = [2, 2, 3, 3, 4, 5,5, 6, 1, 9]
# uniques = []
# for number in numbers:
#     if number not in uniques:
#         uniques.append(number)
# print(uniques)
# tuples
# numbers = (1, 2, 3) #            we use () to define tuples
# # numbers[0] = 10
# print(numbers[0])

# unpacking
# coordinates = (1, 2, 3)
# print(coordinates[0]* coordinates[1]* coordinates[2])
# x = coordinates[0]
# y = coordinates[1]
# z= coordinates[2]
# x, y, z = coordinates # unpacking - this is called unpacking
# print(x*y*z)
# print(x, y, z)
# Dictionaries in python - key :value pair dictionary - define dictionary
# customer = {
#     "name": "Aradhana Singh",
#     "age": 34,
#     "is_verified": True
# }
# print(customer["name"], customer["age"])
# print(customer.get("birthdate", "15th Jul 1985"))  # can add value
# example
# phone = input("Phone: ")
# digits_mapping = {
#     "1": "One",
#     "2": "Two",
#     "3": "three"
# }
# output = ""
# for ch in phone:
#   output +=  digits_mapping.get(ch, " !") + "\n"
# print(output)
# example2
# message = input(">")
# words = message.split(' ')
# emojis = {
#     ":)": "🙂",
#     ":D": "🙋",
#     ":(": "😢"
# }
# output = ""
# for word in words:
#     output += emojis.get(word, word) + " "
# print(words)
# print(output)
# Functions ****************************
# def greet_user(name):
#     print(f'hi {name} !')
#     print("Welcome aboard")
#
# Note: parameter is placeholder and argument is actual value of parameter reference
# greet_user("Aradhana")
# def greet_user(first_name, last_name):
#     print(f'hi {first_name} {last_name}!')
#     print("Welcome aboard")
#
#
# greet_user("Aradhana", "Singh")   # first_name= "Aradhana" can be used then order of arguments will not matter else it does

## Return statement

# def square(number):
#     return number * number
#
# # Note : by default python returns None for any function
# print(square(3))
## Refactor , reorgnise or optimize the code
# def emoji_converter(message):
#     words = message.split(' ')
#     emojis = {
#         ":)": "🙂",
#         ":D": "🙋",
#         ":(": "😢"
#     }
#     output = ""
#     for word in words:
#         output += emojis.get(word, word) + " "
#     return output
#
#
# message = input("> ")
# emoji_converter(message)
# print(emoji_converter(message))

## Handle Errors , Exceptions*************
try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Age can not be 0.')
except ValueError:
    print("Invalid value")

## Comments in python  - Avoid explaining what the code does as that may change. use comment to explain why and how not what

## CLASSES in python
