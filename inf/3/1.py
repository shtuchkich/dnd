n = int(input())
a = [0, 1] + [0] * n 
for i in range (2, len(a)):
    x = a[i - 2]
    y = a[i - 1]
    a[i] = x + y
print(a[n])
    