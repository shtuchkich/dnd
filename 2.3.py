def z(s):
    s1 = ''
    for el in 'QRPDFGKCBN04679':
        if el in s:
            return 0
    for el in s:
        if s == 'E':
            s1 += '3'
        elif s == '3':
            s1 += 'E'
        elif s == 'J':
            s1 += 'L'
        elif s == 'L':
            s1 += 'J'
        elif s == 'S':
            s1 += '2'
        elif s == '2':
            s1 += 'S'
        elif s == 'Z':
            s1 += '5'
        elif s == '5':
            s1 += 'Z'
        else:
            s1 += el
    return s1
s = input()
s1 = z(s)
if s == s[::-1]:
    if s1 != 0:
        print(s + ' is a mirrored palindrome')
    else:
        print(s + ' is a regular palindrome')
else:
    if s1 != 0:
        print(s + ' is morrored string')
    else:
        print(s + ' is not a palindrome')