def user_name():
    name = 'Вова'
    surname = 'Петров'
    age = 28
    return name, surname, age


user = user_name()
print()
print('***', *user)
print(f'\nЧерез " return " можно вывести много значений: {user}')
