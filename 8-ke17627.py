import itertools as it

'''
ans = 0
for val in it.product(range(15), repeat=5):
    if val[0] == 0: continue

    c8 = 0
    c9 = 0
    for v in val:
        if v == 8:
            c8 += 1
        if v > 9:
            c9 += 1

    if c8 == 1 and c9 >= 2:
        ans += 1

print(ans)
'''
ans = 0
for val in it.product(range(15), repeat=5):
    if val[0] == 0: continue

    c8 = len([v for v in val if v == 8])
    c9 = len([v for v in val if v > 9])
    
    if c8 == 1 and c9 >= 2:
        ans += 1

print(ans)