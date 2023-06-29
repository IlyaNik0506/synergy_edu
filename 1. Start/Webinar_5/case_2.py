key = input('Введите ключ активации: ')
history_key = ['123', 'aaa']


def activ_key(key):
    if key in history_key:
        return 'Данный код уже был использован'
    else:
        history_key.append(key)
        print(history_key)
        return 'Продукт активирован'


print(activ_key(key))
