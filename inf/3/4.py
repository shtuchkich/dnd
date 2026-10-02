n = input().split()
a = int(n[0])
b = n[1]
maxos = a // 2 + a % 2
for i in range (1, a + 1):
    if i <= maxos:
        print (b * i)
    if (i > maxos):
        print(b * (a + 1 - i))


