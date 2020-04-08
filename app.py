# Car Game

# command = ''
# started = False
# while True:
#     command = input("> ").lower()
#     if command == "start":
#         if started:
#             print("Car is already started.....!")
#         else:
#             started = True
#             print("Car Started....")
#     elif command == "stop":
#         if not started:
#             print("Car is already stopped")
#         else:
#             started = False
#             print("Car stopped!")
#     elif command == "help":
#         print('''
# start - to dtart the car
# stop - to stop the car
# quit - to quit
#                ''')
#     elif command == "quit":
#         break
#     else:
#         print("Sorry, I don't understand")
# for item in "Python":
#     print(item)
# for arr in ["Aradhana", "Singh"]:
#     print(arr)

# for item in range(5, 10, 2):  # 2 steps forward
#     print(item)
# prices = [10, 20, 30]
# total = 0
# for price in prices:
#     total +=  price
# print(f"total: {total}")
# Nested loop (x,y), (0,0).....
# for x in range(4):
#     for y in range(3):
# #         print(f'({x}, {y})')
# numbers = [5, 2, 5, 2, 2]
# for item in numbers:
#     # print('x'* item)
#     output = ''
#     for count in range(item):
#         output += 'x'
#     print(output)
# names = ["Aradhana", "Anu", "Rahul"]
# names[0] = "Neha"
# print(names[0:]) # 1:3 , -1 -2 , :2 etc
numbers = [3, 6, 2, 8, 4, 10, 13]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)
