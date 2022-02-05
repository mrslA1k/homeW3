print('Написать декоратор inspect, который при вызове фунцкии печатает входные параметры и возвращаемое значение,')
print('обвернуть в него функцию contact.')

str = input("Введите список (разделитель пробел): ")
rev = input("Выводить в обратном порядке? (y или n): ")
if rev == "y":
    s_rev:bool = True
else:
    s_rev:bool = False

if str == '':
    print("Список не заполнен.")
else:
    str_add = str.split()

    def inspect(function):
       def wrapper(str, key=s_rev):
        print(f'входные параметры str: {str}, key: {key}')
        rez_func = function(str, key)
        print(f'выходные параметры функции: {rez_func}')
        return 'End'
       return wrapper

    @inspect
    def contact(str,reversed=s_rev):
      if reversed is True:
        str.reverse()
      str_out = ''
      for i in str:
        str_out += i + ' '
      return str_add

print(contact(str_add, s_rev))

print("Bye")
input("жмякни Интер для выхода")