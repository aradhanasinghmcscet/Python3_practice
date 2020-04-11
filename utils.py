def find_max(numbers):
    max1 = numbers[0]
    for number in numbers:
        if number > max1:
            max1 = number
    return max1
