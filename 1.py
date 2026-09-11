n = int(input())
a = input()
a = list(map(int, a.split(' ')))
for i in range (1, n + 1):
    if i not in a:
        print(i)
        break