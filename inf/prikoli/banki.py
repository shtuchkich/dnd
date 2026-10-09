N = int(input())
k = int(input())
a = []
for i in range (k):
    x = int(input())
    a.append(x)

d = {0: 0}
a = sorted(a)
for i in range (N // a[0] + 1):
    d1 = list(d.keys())
    for sum in d1:
        for el in a:
            if (sum + el) not in d and (sum + el) <= N:
                d[sum + el] = el
if N in d:
    res = {el: 0 for el in a}
    while N > 0:
        res[d[N]] += 1
        N = N - d[N]
    print(res)
else:
    print('Net') 
        
        
