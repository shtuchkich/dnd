import matplotlib.pyplot as plt
import math as m
file = open("result2.txt")
a = []
for el in file:
    if el.strip() != '':
        a.append(el.strip())
a10 = []
a20 = []
a40 = []
a80 = []
b10 = []
b20 = []
b40 = []
b80 = []
for i in range (len(a)):
    if i % 10 == 0:
        a10.append(sum(b10))
        b10 = []
    if i % 20 == 0:
        a20.append(sum(b20))
        b20 = []
    if i % 40 == 0:
        a40.append(sum(b40))
        b40 = []
    if i % 80 == 0:
        a80.append(sum(b80))
        b80 = []
    b10.append(int(a[i]))
    b20.append(int(a[i]))
    b40.append(int(a[i]))
    b80.append(int(a[i]))


w10 = []
w20 = []
w40 = []
w80 = []
n10 = sum(a10) / (len(a10) - 1)
n20 = sum(a20) / (len(a20) - 1)
n40 = sum(a40) / (len(a40) - 1)
n80 = sum(a80) / (len(a80) - 1)
d10 = 0
d20 = 0 
d40 = 0
d80 = 0
s10 = list(set(sorted(a10[1::])))
for el in a10[1::]:
    d10 += (el - n10) ** 2
for el in a20[1::]:
    d20 += (el - n20) ** 2
for el in a40[1::]:
    d40 += (el - n40) ** 2
for el in a80[1::]:
    d80 += (el - n80) ** 2

d10 = (d10 / (len(a10) - 1) ** 0.5)
d20 = (d20 / (len(a20) - 1) ** 0.5)
d40 = (d40 / (len(a40) - 1) ** 0.5)
d80 = (d80 / (len(a80) - 1) ** 0.5)

dd10 = d10 / ((len(a10) - 1) ** 0.5)
dd20 = d20 / ((len(a20) - 1) ** 0.5)
dd40 = d40 / ((len(a40) - 1) ** 0.5)
dd80 = d80 / ((len(a80) - 1) ** 0.5)

j10 = n10 / 10
j20 = n20 / 20
j40 = n40 / 40
j80 = n80 / 80

dj10 = dd10 / 10
dj20 = dd20 / 20
dj40 = dd40 / 40
dj80 = dd80 / 80

p10 = []
p20 = []
p40 = []
p80 = []

g10 = []
g20 = []
g40 = []
g80 = []

for el in s10:
    w = a10[1::].count(el) / len(a10)
    w10.append(w) 
    p = (n10 ** el) * (m.e ** -n10) / m.factorial(el)
    p10.append(p)
    g = (1 / dd10 / ((2 * 3.14) ** 0.5)) * (m.e ** (-1 * (el / 2 * dd10 ** 2)))
s20 = list(set(sorted(a20[1::])))
for el in s20:
    w = a20[1::].count(el) / len(a20)
    w20.append(w)
    p = (n20 ** el) * (m.e ** -n20) / m.factorial(el)
    p20.append(p)
s40 = list(sorted(set(a40[1::])))
for el in s40:
    w = a40[1::].count(el) / len(a40)
    w40.append(w)
    p = (n40 ** el) * (m.e ** -n40) / m.factorial(el)
    p40.append(p)
s80 = list(set(sorted(a80[1::])))
s80.append(s80[0])
s80 = s80[2::]
for el in s80:
    w = a80[1::].count(el) / len(a80)
    w80.append(w)
    p = (n80 ** el) * (m.e ** -n80) / m.factorial(el)
    p80.append(p)
plt.step(s10, w10)
plt.step(s20, w20)
plt.step(s40, w40)
plt.step(s80, w80)
plt.plot(s10, p10)
plt.plot(s20, p20)
plt.plot(s40, p40)
plt.plot(s80, p80)
plt.plot(s10, g10, color = "red")
plt.xlabel('n')
plt.ylabel('w')
plt.show()


yli1 = 0
yli2 = 0
yli3 = 0 
for el in a10[1::]:
    if abs(el - n10) <= d10:
        yli1 += 1 
    if abs(el - n10) <= 2 * d10:
        yli2 += 1
    if abs(el - n10) <= 3 * d10:
        yli3 += 1
print(yli1, yli2, yli3)

yli1 = 0
yli2 = 0
yli3 = 0 
for el in a20[1::]:
    if abs(el - n20) <= d20:
        yli1 += 1 
    if abs(el - n20) <= 2 * d20:
        yli2 += 1
    if abs(el - n20) <= 3 * d20:
        yli3 += 1
print(yli1, yli2, yli3)

yli1 = 0
yli2 = 0
yli3 = 0 
for el in a40[1::]:
    if abs(el - n40) <= d40:
        yli1 += 1 
    if abs(el - n40) <= 2 * d40:
        yli2 += 1
    if abs(el - n40) <= 3 * d40:
        yli3 += 1
print(yli1, yli2, yli3)

yli1 = 0
yli2 = 0
yli3 = 0 
for el in a80[1::]:
    if abs(el - n80) <= d80:
        yli1 += 1 
    if abs(el - n80) <= 2 * d80:
        yli2 += 1
    if abs(el - n80) <= 3 * d80:
        yli3 += 1
print(yli1, yli2, yli3)