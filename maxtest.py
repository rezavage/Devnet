from findmax import find_max

numbers=[0]
i = 10
while i > 0:
    x = input("enter a value: ")
    i -= 1
    numbers.append(x)

print(numbers)
r = find_max(numbers)
print(f'the maximum number is {r}')
