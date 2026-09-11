n = int(input())
s = input()
s1 = ''
x = len(s) // n
for i in range (x):
    s1 += s[i * n: (i + 1) * n][::-1]
print(s1)