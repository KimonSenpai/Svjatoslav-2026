
'''
95 = 1011111
96 = 1100000
100 = 1100100
99 = 1100011
'''


res = []

for i in range(1, 1000):
    n = bin(i)[2:] # -> '0b00110' убираем первые два символа
    if i % 2 == 0:
        n = '11' + n + '11'
    else:
        n = '1' + n + '00'

    res.append(int(n, base=2))

res.sort()

res = [x for x in res if 95 <= x]

print(res[0:10])