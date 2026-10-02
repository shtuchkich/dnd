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
a = int(input())
b = int(input())
z1 = deli(a)
z2 = deli(b)
z3 = list(set(z1 + z2))
nod = 1
for i in range (len(z3)):
    nod *= z3[i] ** min(z1.count(z3[i]), z2.count(z3[i]))
a1 = a // nod
b1 = b // nod
r = []
for x in range (-1 * a * b, a * b):
    for y in range (-1 * a * b, a * b):
        if x * a1 + y * b1 > 1:
            break
        if x * a1 + y * b1 == 1:
            r.append([abs(x) + abs(y), x, y])
r = sorted(r)
print(r[0][1], r[0][2])
