x = input()
y = input()
x = list(map(int, x.split()))
y = list(map(int, y.split()))
xy = 0 * 7
xx = 0 * 7
x1 = sum(x) / len(x)
y1 = sum(y) / len(y)
k1 = 0
for i in range (len(x)):
    xy += x[i] * y[i]
    xx += x[i] ** 2
xy = xy / len(x)
xx = xx / len(x)
k = (xy - x1 * y1) / (xx - x1 * x1)
b = y1 - k * x1
print(k, b)
