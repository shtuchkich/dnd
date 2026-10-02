n = int(input())
a = input()
a = list(map(int, a.split(' ')))
mini = 100000000000
for i in range(n):
    x = a[i]
    k = 0
    l = 0            
    ravn = 0
    for j in range(n):
        if i == j:
            continue
        else:
            y = a[j]
            if x > y :
                k += 1
            if x < y:
                l += 1
            if x == y:
                ravn += 1
    if (k <= n // 2) and (k + ravn >= n // 2):
        print(x)
        break
        