'''
Определите количество шестизначных чисел, 
записанных в семеричной системе счисления, 
которые не оканчиваются на цифры, меньшие 4, 
а также содержат поровну четных и нечетных цифр.
'''

from itertools import product

ans = 0

for val in product(range(7), repeat=6):
    if val[0] == 0: continue
    ch = 0
    for v in val:
        if v % 2 == 0:
            ch += 1

    if ch == 3 and val[-1] >= 4:
        ans += 1

print(ans)