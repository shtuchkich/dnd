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

n = int(input())
m = int(input())
a = []
for i in range (n):
    s = input()
    s = list(map(int, s.split()))
    a.append(s)
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