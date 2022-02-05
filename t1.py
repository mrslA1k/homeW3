print('Создать функцию contact, котроая принимает неограниченное количество параметров-строк их склеивает и возвращает.')
print('Опционально может принимать именнованный параметр reversed: bool и при reversed=True склеивание начинается с конца списка параметров.')

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


    def contact(str,reversed=s_rev):
     if reversed is True:
      str.reverse()

     str_out = ''
     for i in str:
      str_out += i + ' '
     return str_add

    print(contact(str_add))

print("Bye")
input("жмякни Интер для выхода")
