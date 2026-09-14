import itertools as it # удобный перебор
import functools as ft # инструменты для функций. Для нас lru_cache
import turtle
import re

'''
x   y   x->y
0   0   1
0   1   1
1   0   0
1   1   1
'''
'''
Если угол A прямой => треугольник АВС прямоугольный
'''

def impl(x, y):
    return x <= y

print('x y z w')
print('-------')

'''
for x in [0, 1]:
    for y in [0, 1]:
'''

for x, y, z, w in it.product([0, 1], repeat=4):
    if not(impl(x == (not y), not impl(w, x)) or not z):
        print(x, y, z, w)
