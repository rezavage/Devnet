def find_max(numbers):
    maximum = numbers[0]
    for number in numbers:
        if int(number) > int(maximum):
            maximum = number
    return maximum

