__author__ = 'Ивлиев Сергей Владимирович'

# 1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

print('Задание 1')
my_long_list = ['Bitcoin', 'Swiss Franc', 810, 3.14, 'Constant', None]
str_count = 0
int_count = 0
float_count = 0
none_count = 0
for my_element in my_long_list:
#    print(my_element,type(my_element))
    if type(my_element) == str: str_count += 1
    if type(my_element) == int: int_count += 1
    if type(my_element) == float: float_count += 1
    if my_element == None: none_count += 1
print(str_count,'strings')
print(float_count,'floating point numbers')
print(int_count,'integers')
print(none_count,'nones')
print('')

# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().

print('Задание 2')
my_unknown_list = list(map(int,input('Введите элементы массива через пробел ').split()))
print(my_unknown_list)
my_sorted_list = my_unknown_list.copy()
i = 0
while i < len(my_unknown_list) - 1:
    my_sorted_list[i + 1] = my_unknown_list[i]
    my_sorted_list[i] = my_unknown_list[i + 1]
    i += 2
print(my_sorted_list)
print('')

# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

print('Задание 3')
print('Введите номер месяца от 1 до 12')
month_number = int(input())
months_details = ['зима', 'зима', 'весна','весна','весна','лето','лето','лето','осень','осень','осень','зима']
if month_number > 12:
    print('Номер месяца не может быть больше 12')
else:
    if month_number < 1:
        print('Номер месяца не может быть меньше 1')
    else:
        print('Это', months_details[month_number-1])

# Реализация через dict.
months_dict = dict(key_1='зима', key_2='весна', key_3='лето', key_4='осень')
if month_number > 12:
    print('Номер месяца не может быть больше 12')
else:
    if month_number < 1:
        print('Номер месяца не может быть меньше 1')
    else:
        if month_number // 3 == 4:
            print('Да, это',months_dict.get('key_' + str(1)))
        else:
            print('Да, это', months_dict.get('key_'+str(month_number//3+1)))
print('')


# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

print('Задание 4')
my_unknownword_list = list(map(str,input('Введите предложение ').split()))
j = 1
for my_element in my_unknownword_list:
    print(j, my_element[0:10])
    j += 1
print('')


# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
print('Задание 5')
my_rating = [7, 5, 3, 3, 2]
while len(my_rating) < 10:
    print('Введите новый элемент рейтинга')
    new_element = int(input())
    my_rating.append(new_element)
    my_rating.sort()
    my_rating.reverse()
    print(my_rating)