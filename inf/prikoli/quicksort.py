def f(a):
    if len(a) == 0:
        return ['']
    if len(a) == 1:
        return a
    n = len(a) // 2
    x = []
    b = []
    c = []
    for i in range(a.count(a[n])):
        x.append(a[n])
    for el in a:
        if el > x[0]:
            b.append(el)
        if el < x[0]:
            c.append(el)
    return f(c) + x + f(b)


s = input()
s = list(map(int, s.split()))
res = f(s)
fin = []
for el in res:
    if el != '':
        fin.append(el)
print(fin)