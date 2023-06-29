start = int(input('Введите 1-е число: '))
end = int(input('Введите 2-е число: '))


def get_primes_from_range(start, end):
    ls = []
    for i in range(start, end+1):
        if i == 1:
            pass
        elif i == 2:
            ls.append(i)
        else:
            for x in range(2, i):
                if i % x == 0:
                    break
            else:
                ls.append(i)
    return ls


print(get_primes_from_range(start, end))

