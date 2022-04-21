def type_check(arr):
    x = list()
    if isinstance(arr, dict):
        for n, s in enumerate(arr):
            if n % 2 == 0:
                x.append(arr[s])
    else:
        for n, s in enumerate(arr):
            if n % 2 == 0:
                x.append(s)

    return x


such_text = 'О Дивный Новый мир!'
such_list = [100, 200, 300, 400, 'буква', 0, 2, 'а']
such_tuple = (100, 200, 300, 400, 'буква', 0, 2, 'а')
such_dictionary = {1: 100, 2: 200, 3: 300, 4: 400, 5: 'буква', 6: 0, 7: 2, 8: 'а'}

print(f'Результат: {type_check(such_text)}')
print(f'Результат: {type_check(such_list)}')
print(f'Результат: {type_check(such_tuple)}')
print(f'Результат: {type_check(such_dictionary)}')
