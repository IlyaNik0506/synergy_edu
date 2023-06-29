from random import randint

z = randint(0, 1000)


def rand(z):
    y = 0
    while y < 20:
        x = int(input())
        if x > z:
            y += 1
            print('Меньше')
            continue
        elif x < z:
            y += 1
            print('Больше')
            continue
        else:
            y += 1
            print('Угадал!')
            break


rand(z)