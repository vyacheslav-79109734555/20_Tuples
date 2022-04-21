scores_dict = {
    'Петя': 60
}
for name in scores_dict.items():  # items
    print(f'Вывод кортежей: {name}')
for name, scores in scores_dict.items():  # items
    print(f'1 - {name} : {scores}')
for name, scores in scores_dict.items():  # items
    print(f'2 - {name}')
for name, scores in scores_dict.items():  # items
    print(f'3 - {scores}')
for name in scores_dict:
    print(f'4 - {name} : {scores_dict[name]}')
print('************************')

score_dict = {
    (5000, 123456): ('Иванов', 'Василий')
}
for name, scores in score_dict.items():  # items
    print(f'1 - {name} : {scores}')
for name, scores in score_dict.items():  # items
    print(f'1 - {name[0]} {name[1]} : {scores[0]} {scores[1]}')
