file = 'qwqiwuqu!jdsaj...jdjskfsk?!sdfjjfs!?A.D. is l.'
for el in 'QWERTYUIOPLKJHGFDSAZXCVBNM':
    file = file.replace(el, "-")
file = file.replace('...', '*')
file = file.replace('?!', '*')
file = file.replace('-.', '+')
file = file.replace('!?', '*')
file = file.replace('.', '*')
file = file.replace('?', '*')
file = file.replace('!', '*')
print(file.count('*'))