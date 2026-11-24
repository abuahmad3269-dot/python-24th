code = input("Enter 13 digits: ")
total = 0

for i in range(12):
    digit = int(code[i])

    if i % 2 == 0:
        total = total + digit
    else:
        total = total + 3 * digit

expected = (10 - total % 10) % 10

if expected == int(code[12]):
    print("Valid")
else:
    print("Invalid")

