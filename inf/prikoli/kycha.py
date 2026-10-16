def heap(a):
    n = len(a)
    for i in range (n // 2 - 2 + n % 2, -1, -1):
        c = [a[i], a[2 * i + 1], a[2 * i + 2]]
        c[1] = sum(c) - min(c) - max(c)
        c[0] = min(a[i], a[2 * i + 1], a[2 * i + 2])
        c[2] = max(a[i], a[2 * i + 1], a[2 * i + 2])
        a[i] = c[0]
        a[2 * i + 1] = c[1]
        a[2 * i + 2] = c[2]
    return a



s = input()
s = list(map(int, s.split()))
b = []
for i in range (len(s)):
    s = heap(s)
    b.append(s[0])
    s = s[1::]
print(b)
