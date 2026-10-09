import matplotlib.pyplot as plt
def det(m):
    s = 0
    if len(m) == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]
    for w in range (len(m)):
        m1 = []
        s1 = m[0][w]
        for i in range (1, len(m)):
            jz = 0
            x = [0] * (len(m) - 1)
            for j in range (len(m)):
                if j == w:
                    jz -= 1
                if j != w:
                    x[jz] = m[i][j]
                jz += 1
            m1.append(x)
        s = ((-1) ** w) * s1 * det(m1) + s
    return s

T = [4.48, 4.46, 4.48, 4.44, 4.45, 4.46, 4.46, 4.47, 4.47, 4.48]
d = 0
s = sum(T) / 10
for el in T:
    d += (el - s) ** 2
d = (d / 10) ** 0.5
print(s, d)

print(((2 * 2.17 * 1 / (2.17 ** 2 - (0.1154 - 0.0305) ** 2) ** 0.5 * 0.001) ** 2 + (2 * (0.1154 - 0.0305) * 1 / (2.17 ** 2 - (0.1154 - 0.0305) ** 2) ** 0.5 * 0.0005) ** 2 + (2 * (0.1154 - 0.0305) * 1 / (2.17 ** 2 - (0.1154 - 0.0305) ** 2) **0.5 * 0.0003) ** 2) ** 0.5)
print(((0.0005 * 10 * 0.0305 / 4 / 3.14 / 3.14 / 2.17) ** 2 + (0.0003 * 10 * 0.1154 / 4 / 3.14 / 3.14 / 2.17) ** 2 + (0.02 * 10 * 0.1154 * 0.0305 / 4 / 3.14 / 3.14 / 2.17 / 2.17) ** 2) ** 0.5)
T = [[3.09, 3.08], [3.09, 3.08], [3.11, 3.12], [3.15, 3.14], [3.2, 3.17], [3.24, 3.25], [3.31, 3.3], [3.38, 3.38]]
m1 = 0.7637
m2 = 0.764
R = 0.0435
I_ter = []
I_exp = []
H = []
x1 = 0
x2 = 0
x3 = 0
x4 = 0
x2y = 0
xy = 0
y = 0
for i in range (len(T)):
    h = 0.005 * i
    x = 0.0004 * (m1 + m2 + 0.9935) * (sum(T[i]) / 2) ** 2 - 0.0079
    I_exp.append(x)
    x1 += h
    x2 += h ** 2
    x3 += h ** 3
    x4 += h ** 4
    x2y += h ** 2 * x
    xy += h * x
    y += x
    x_ter = (m1 + m2) * (R ** 2 / 2 + h ** 2)
    I_ter.append(x_ter)
    H.append(h)
for i in range (len(I_exp)):
    print(I_exp[i], I_ter[i])
n = 3
m = 4
a = [[x4, x3, x2, x2y], [x3, x2, x1, xy], [x2, x1, 8, y]]
b = []
c = []
for i in range (n):
    x = [0] * (n)
    for j in range (m - 1):
        x[j] = a[i][j]
    c.append(x)
    b.append(a[i][-1])
dc = det(c)
n = len(b)
for w in range (n):
    mat = []
    for i in range(n):
        dx = []
        for j in range (n):
            if j != w:
                dx.append(c[i][j])
            if j == w:
                dx.append(b[i])
        mat.append(dx)
    print(det(mat) / dc)
k1 = 1.4780534999999635
k2 = 0.003765322157142865
k3 = 0.0016803047285000267
I_mnk = []
s = 0
for i in range (8):
    h = 0.005 * i
    x = k1 * (h ** 2) + k2 * h + k3
    s += (I_exp[i] - x) ** 2
    I_mnk.append(x)
s = s / 5
s = s ** 0.5
plt.errorbar(H, I_mnk, xerr = 0, yerr = s, color = "green", ecolor = "red")
plt.xlabel('H')
plt.ylabel('I')
plt.show()