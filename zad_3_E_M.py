# Напишите программу, которая запрашивает у пользователя число, а затем выводит "Четное", если число четное, 
# или "Нечетное", если число нечетное

import math
import sys

def check_even_odd(number):
    """Проверяет, четное ли число."""
    return "Четное" if number % 2 == 0 else "Нечетное"

def factorize(number):
    """Разлагает число на множители."""
    factors = []
    for i in range(1, int(math.sqrt(number)) + 1):
        if number % i == 0:  # Если остатка нет, значит множитель
            factors.append(i)
            factors.append(number // i)
    # Преобразуем во множество, чтобы избавиться от повторов
    factors = list(set(factors))
    factors.sort()
    return factors

def main():
    print("Добро пожаловать в программу проверки четности и разложения на множители!")
    
    while True:
        print("\nВыберите действие:")
        print("1 - Проверка четности или нечетности числа")
        print("2 - Разложение на множители числа")
        print("0 - Выход из программы")
        
        choice = input("> ")
        
        if choice == '0':
            print("До свидания, спасибо что воспользовались нашей программой.")
            break
        elif choice == '1':
            response = input("Введите целое число: ")
            if not response.isdecimal():
                print("Ошибка: введите положительное целое число.")
                continue
            number = int(response)
            result = check_even_odd(number)
            print(f"Число {number} является: {result}.")
        elif choice == '2':
            response = input("Введите положительное целое значение коэффициента: ")
            if not (response.isdecimal() and int(response) > 0):
                print("Ошибка: введите положительное целое число.")
                continue
            number = int(response)
            factors = factorize(number)
            print(f"Множители числа {number}: {', '.join(map(str, factors))}.")
        else:
            print("Ошибка: неверный выбор. Пожалуйста, выберите действие из меню.")

if __name__ == "__main__":
    main()
