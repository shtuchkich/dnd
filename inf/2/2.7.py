a = input()
a = list(map(int, a.split(' ')))
maxi = 0
maxos = 0
for el in a:
    if a.count(el) > maxi:
        maxi = a.count(el)
        maxos = el
print(maxos)
