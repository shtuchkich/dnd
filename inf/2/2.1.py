n = int(input())
a = input()
a = list(map(int, a.split(' ')))
s = sum(a)
s1 = (1 + n) / 2 * n
print(int(s1 - s))