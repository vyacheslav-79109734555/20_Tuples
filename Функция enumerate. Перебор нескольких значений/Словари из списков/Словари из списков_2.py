import random

arr = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

txt_list_1 = list(arr[random.randint(0, 32)] for _ in range(10))
print(f'Первый список: {txt_list_1}')

txt_list_2 = list(arr[random.randint(0, 32)] for _ in range(10))
print(f'Второй список: {txt_list_2}\n')

txt_dict_1 = {num: txt for num, txt in enumerate(txt_list_1)}
print(f'Первый словарь: {txt_dict_1}')

print(f'Второй словарь:', {num: txt for num, txt in enumerate(txt_list_2)})
