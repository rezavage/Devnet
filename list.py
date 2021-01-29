numbers=[1,3,2,4,7,6,5,8,3,5,3,3,4]
checks=[]
for index in numbers:
    if index not in checks:
        checks.append(index)
print (checks)



