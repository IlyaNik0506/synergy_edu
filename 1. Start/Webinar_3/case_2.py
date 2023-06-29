def sum_buy():
    print('Как закончите вводить покупки, введите "0"')
    sum_price = 0
    while True:
        x = float(input('Введите стоимость покупки: '))
        if x == 0:
            break
        sum_price += x
    return sum_price


def sale(price):
    price_sale = price / 10
    res = price - price_sale
    return res


price = sum_buy()

print(f'Общая сумма покупок: {price}')
print(f'Общая сумма с учетом 10% скидки: {sale(price)}')
