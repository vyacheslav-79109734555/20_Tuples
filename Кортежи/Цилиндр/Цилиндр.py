import math


def side_full(radius, height):
    sid = 2 * math.pi * radius * height
    ful = sid + 2 * math.pi * radius ** 2
    return round(sid, 2), round(ful, 2)


r = float(input('Введите радиус: '))
h = float(input('Введите высоту: '))
side, full = side_full(r, h)
print(f'Площадь боковой фигуры: {side}\nПолная площадь: {full}')
