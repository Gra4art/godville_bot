import requests

username = input('Введите логин: ')
password = input('Введите пароль: ')

def login(username, password):
    global session
    session = requests.Session()
    session.post('https://godville.net/login/login', data = {
                 'username': username,
                 'password': password,
                 })

    test_page = session.get('https://godville.net/news')
    test_text = 'Приветствуем, о'
    if test_text in test_page.text:
        print('Логгинг прошёл удачно')
    else:
        print('Залогиниться не удалось')


login(username, password)