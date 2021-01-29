weight = input('Enter your weight: ')
unit = input('Enter (K)g or (L)bs: ')
if unit.upper() == "K":
    print(f'your body weight is', int(weight)*2, 'Lbs')
elif unit.upper() == "L":
    print(f'your body weight is', int(weight)/2, 'Kg')
else:
    print(f'The unit is unknown')