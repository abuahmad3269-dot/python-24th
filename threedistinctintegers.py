
target = int(input("Target sum: "))

for a in range(1, 10):
    for b in range(a + 1, 10):
        for c in range(b + 1, 10):
            if a + b + c == target:
                print(a, b, c)

