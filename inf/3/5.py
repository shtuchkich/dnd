n = int(input())
m = int(input())
a = [m * [0]] * n
for i in range (n):
    x = a[i]
    for j in range (m):
        x[j] = j + 1
    a[i] = x
for i in range (len(a)):
    print(a[i], end = '\n')