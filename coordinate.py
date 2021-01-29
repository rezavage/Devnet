numbers = {
    "1":"one",
    "2":"two",
    "3":"Three",
    "4":"four",
    "5":"five"
}
output = ""
x = input('enter your phone number')
for s in x:
    output += numbers.get(s, " !")+ " "
print(output)

