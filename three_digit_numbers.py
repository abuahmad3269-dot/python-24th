n = 0
for n in range(100, 1000):
    a = n // 100
    b = (n // 10) % 10
    c = n % 10
    if a*a + b*b + c*c == n:
        print(n)

