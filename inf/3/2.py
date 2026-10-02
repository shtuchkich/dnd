def deli(n):
    x = 2
    a = []
    while x * x <= n:
        while n % x == 0:
            a.append(x)
            n = n // x
        x += 1
    if n > 1:
        a.append(n)
    return a
n = int(input())
print(deli(n))