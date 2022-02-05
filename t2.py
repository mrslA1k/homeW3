print('Написать рекурсивную функцию factorial, которая считает факториал числа.')
print('(factorial() = 1*2*...*n).')

n = input('Введите число: ')
def factorial(n):
    f = 1
    if n >= 1:
        f = n * factorial(n - 1)
    return f

print(f'Facrotial: {factorial(5)}')

print("Bye")
input("жмякни Интер для выхода")