
def three(val):
    res = ''
    while val > 0:
        res = str(val % 3) + res
        val //= 3
    return res

def three_rec(val):
    if val == 0:
        return ''
    return three_rec(val // 3) + str(val % 3)

res = []
for i in range(1,150):
    n = three(i)
    if i % 3 == 0:
        n += n[-2:]
    else:
        n += three(i % 3 * 5)

    r = int(n, base=3)
    if r > 150:
        res.append(r)

print(min(res))