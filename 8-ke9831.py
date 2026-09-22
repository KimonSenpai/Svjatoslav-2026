import itertools as it

it.product # произведение Декарта
it.permutations # перестановки
it.combinations # комбинации

ans = 0
for val in it.product(range(16), repeat=3):
    if val[0] == 0: continue

    if len(set(val)) != len(val): continue

    if not all(v%2 != w%2 for v, w in zip(val, val[1:])): continue


    ans += 1

print(ans)
