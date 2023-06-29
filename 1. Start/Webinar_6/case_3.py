xp = float(input('Введите xp: '))
yp = float(input('Введите yp: '))
xo = float(input('Введите xo: '))
yo = float(input('Введите yo: '))
r = float(input('Введите r: '))


def check_point_belongs_circle(xp, yp, xo, yo, r):
    if (xp - xo) ** 2 + (yp - yo) ** 2 <= r ** 2:
        return True
    else:
        return False
