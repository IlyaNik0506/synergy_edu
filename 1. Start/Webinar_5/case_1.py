def set_number():
    num = set()
    print('В конце введите 0 ')
    while True:
        number = int(input('Введите число: '))
        num.add(number)
        if number == 0:
            num.remove(number)
            break
    return len(num)


print(f'Введено уникальных чисел: {set_number()}')
