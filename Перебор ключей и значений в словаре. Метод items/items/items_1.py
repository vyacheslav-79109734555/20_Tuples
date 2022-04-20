scores_dict = {
    'Ваня': 33,
    'Петя': 60,
    'Лена': 45
}

for name in scores_dict.items():  # items
    print(f'Вывод кортежей: {name}')

for name, scores in scores_dict.items():  # items
    print(f'{name} : {scores}')

for name, scores in scores_dict.items():  # items
    print(f'{name}')

for name, scores in scores_dict.items():  # items
    print(f'{scores}')

for name in scores_dict:
    print(f'{name} : {scores_dict[name]}')
