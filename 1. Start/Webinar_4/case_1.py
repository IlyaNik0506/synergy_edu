string = str(input('Введите предложение: '))
substring = str(input('Введите что ищем: '))


if substring.lower() in string.lower():
    print('Есть контакт!')
else:
    print('Мимо!')
