# def isPrime(num):
#     if num < 2:
#         return False
#     for k in range(2, num):
#         if num % k == 0:
#             return False
#     return True
#
#
# inp = int(input('Enter a number: '))
#
# if isPrime(inp):
#     print(inp, " is a prime number")
# else:
#     print(inp, " is not a prime number")
def isPrime(num):
    if num < 2:
        return False
    k = 2
    while k * k <= num:
        if num % k == 0:
            return
        k = k+1
    return True


inp = int(input('Enter a number: '))

if isPrime(inp):
    print(inp, " is a prime number")
else:
    print(inp, " is not a prime number")