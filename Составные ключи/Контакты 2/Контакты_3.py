def contact_dict():
    try:
        a = (input('Введите: Фамилию абонента: '), input('Введите: Имя абонента: '))
        if a not in phonebook_dict:
            b = int(input('Введите: номер телефона абонента: '))
            phonebook_dict[a] = b
        else:
            print('Такой контакт уже есть')

    except ValueError:
        print('Введите корректные данные!')


phonebook_dict = {}

while True:
    print(f'Ваша телефонная книга содержит: {len(phonebook_dict)} записей')
    try:
        x = int(input('Добавить контакт да/нет = 0/1:\n'))
        if x == 0:
            contact_dict()
        else:
            for person in phonebook_dict:
                print(f'{person[0]} {person[1]}: {phonebook_dict[person]}')
            break

    except ValueError:
        print('*** Введите корректные данные!')



