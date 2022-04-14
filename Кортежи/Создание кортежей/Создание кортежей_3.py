import random

a = tuple(random.randint(0, 6) for _ in range(10))
print(a)
b = tuple(random.randint(-5, 0) for _ in range(10))
print(b)
c = tuple(sorted({n for n in a} | {n for n in b}))
print(c)
print(f'количество нулей = {c.count(0)}')
