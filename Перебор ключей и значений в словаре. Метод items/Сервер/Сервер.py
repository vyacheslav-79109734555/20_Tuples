server_data = {
    "server": {
        "host": "127.0.0.1",
        "port": "10"
    },
    "configuration": {
        "access": "true",
        "login": "Ivan",
        "password": "qwerty"
    }
}

for config, dictionary in server_data.items():
    print(f'{config}:')
    for key, vales in dictionary.items():
        print(f'    {key}: {vales}')
