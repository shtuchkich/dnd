n = int(input())
m = int(input())
a = [m * [0]] * n
f = 0
for i in range (n):
    x = a[i]
    f += 1
    for j in range (m):
        x[j] = j + 1
        f += 2
    a[i] = x
for i in range (len(a)):
    print(a[i], end = '\n')