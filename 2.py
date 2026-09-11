n = int(input())
s = input()
s1 = ''
x = len(s) // n
for i in range (n):
    s1 += s[i * x: (i + 1) * x][::-1]
print(s1)