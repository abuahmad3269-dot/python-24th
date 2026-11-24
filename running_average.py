total = 0
count = 0

while True:
    num = int(input("Enter number (-1 to stop): "))

    if num == -1:
        break

    total = total + num
    count = count + 1

print("Average =", total / count)

