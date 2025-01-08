import math, sys

while True:
    print('Введите положительное целое значение коэффициента (или ЗАВЕРШИТЕ работу): ')
    response = input('> ')
    if response.upper() == 'QUIT':
        sys.exit()

    if not (response.isdecimal() and int(response) > 0):
        continue
    number = int(response)

    factors = []

    # Поиск множителей числа
    for i in range(1, int(math.sqrt(number)) + 1):
        if number % i == 0: # Если остатка нет, значит множитель
            factors.append(i)
            factors.append(number // i)

    # Преобразуем во множество, чтобы избавится от повторов
    factors = list(set(factors))
    factors.sort()

    # Выводим результаты
    for i, factor in enumerate(factors):
        factors[i] = str(factor)   
    print(', '.join(factors))
