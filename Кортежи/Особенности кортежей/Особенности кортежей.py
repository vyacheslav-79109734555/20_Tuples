numb = (10, 20, 30, 40)

print(f'Обратимся по индексу [1] значение = {numb[1]}')
print(f'Обратимся по срезу [1:] значение = {numb[1:]}')

print(f'\nПроверить кортеж на наличие элемента " 5 "  = {5 in numb}')  # проверить наличие элемента
print(f'index 30 = {numb.index(30)}')

some_list = [1, 2, 3]
some_tuple = tuple(some_list)
print(f'\nСписок {some_list} можно превратить в Кортеж {some_tuple}')

# В кортеже могут храниться не только цифры или строки, но и списки:
numb = ('asd', 10, 20, 30, 40, some_list)
print(f'\n{numb}')

# В кортеже, в хранящемся списке можно заменить значение:
numb = ('asd', 10, 20, 30, 40, some_list)
numb[5][0] = 100
print(f'{numb}')

user = 'Vova', 'Petrov', 28
print(f'\nСоставить кортеж легко: {user}')

# Присвоить переменные кортежу:
name, surname, age = user

print(f'name = {name}')
print(f'surname = {surname}')
print(f'age = {age}')

