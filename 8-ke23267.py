from itertools import product

k = 1
ans = 0
for s in product(sorted("СТРОКА"), repeat=5):
    if k % 2 != 0 and s[0] not in 'АЛ' and s.count('С') == 1:
        ans = k
    k += 1

print(ans)