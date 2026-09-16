
for i in range(100):
    n = bin(i)[2:]
    for _ in range(2):
        if n[-1:] == n[-2:-1]:
            n += '0'
        else: 
            n += '1'
    r = int(n, base=2)
    if r > 93:
        print(i)
        break