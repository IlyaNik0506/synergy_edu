lists = []
while True:
    num = int(input('Введите число: '))
    if num == 0:
        break
    lists.append(num)

sr = len(lists)

print(f'Минимальное число: {min(lists)}')
print(f'Максимально число: {max(lists)}')
print(f'Среднее арифметическое: {sum(lists) / sr}')
