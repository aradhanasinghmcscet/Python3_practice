# def isPalindrome(str):
#     rstr = str[:: -1]
#     if str == rstr:
#         return True
#     else:
#         return False
# inp = input('Enter a string ')
# if isPalindrome(inp):
#     print(inp, " is a Palindrome.")
# else:
#     print(inp, " is not a Palindrome.")

def isPalindromeNum(num):
    k = 0
    orgnum = num
    while num > 0:
        k = k * 10 + num % 10
        num = num // 10  # // can be used
    if k == orgnum:
        return True
    else:
        return False
inp = int(input('Enter a integer: '))

if isPalindromeNum((inp)):
    print(inp, " is a PAlindrome.")
else:
    print(inp, " is not a Palindrome.")