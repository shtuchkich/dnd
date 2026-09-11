n = int(input())
a = input()
a = list(map(int, a.split(' ')))
mini = 100000000000
for i in range(n):
    x = a[i]
    k = 0
    l = 0            
    kol = a.count(x)
    for j in range(n):
        if i == j:
            k = k
            l = l
        else:
            y = a[j]
            kol = a.count(x)
            if x >= y :
                k += 1
            if x < y:
                l += 1
    print(k, l, x)
    if (kol >= n // 2) or (l == n // 2 and k == n // 2):
        print(x)
        break
        