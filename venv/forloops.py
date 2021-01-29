numbers = [5,2,5,200,2,8,50,9]
biggest = 0
for items in numbers:
    if items > int(biggest):
        biggest=items
print(biggest)