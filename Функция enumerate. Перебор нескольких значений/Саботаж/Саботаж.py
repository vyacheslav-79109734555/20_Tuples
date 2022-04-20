txt = list(input('Введите текст: '))
print(txt)
x = 0
print('Индексы символа " ~ " ', end='')
for num, sym in enumerate(txt):
    if sym == '~':
        x += 1
        print(f'{num}', end=' ')
print(f'\nВсего символов ~ (тильда) - {x} шт')
