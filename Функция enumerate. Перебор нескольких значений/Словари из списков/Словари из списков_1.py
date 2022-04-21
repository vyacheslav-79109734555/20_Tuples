txt_list_1 = ['й', 'р', 'с', 'г', 'а', 'а', 'т', 'ж', 'е', 'к']
txt_list_2 = ['д', 'а', 'а', 'в', 'т', 'ж', 'р', 'б', 'й', 'р']
txt_dict_1 = dict()
txt_dict_2 = dict()
for num, txt in enumerate(txt_list_1):
    txt_dict_1.setdefault(num, txt)
print(f'Первый список: {txt_list_1}')

for num, txt in enumerate(txt_list_2):
    txt_dict_2.setdefault(num, txt)
print(f'Второй список: {txt_list_2}\n')
print(f'Первый словарь: {txt_dict_1}')
print(f'Второй словарь: {txt_dict_2}')
