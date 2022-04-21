def contact_dict():
    try:
        a = input('Введите: Фамилию абонента: ')
        b = input('Введите: Имя абонента: ')
        c = int(input('Введите: номер телефона абонента: '))
        d = a[::], b[::]

        if d not in phonebook_dict:
            phonebook_dict[d] = c
        else:
            print('Такой контакт уже есть')

    except ValueError:
        print('Введите корректные данные!')


phonebook_dict = {}

while True:
    try:
        x = int(input('Добавить контакт да/нет = 0/1:\n'))
        if x == 0:
            contact_dict()

        else:
            print(f'Ваша телефонная книга содержит: {len(phonebook_dict)} записей')
            for person in phonebook_dict:
                print(f'{person[0]} {person[1]}: {phonebook_dict[person]}')
            break

    except ValueError:
        print('*** Введите корректные данные!')
