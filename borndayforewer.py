"""
МОДУЛЬ 2
Программа из 2-го дз
Сначала пользователь вводит год рождения Пушкина, когда отвечает верно вводит день рождения
Можно использовать свой вариант программы из предыдущего дз, мой вариант реализован ниже
Задание: переписать код используя как минимум 1 функцию
"""
# *******************************************************************
# ВАРИАНТ 1
# def input_input(stroka):
#     num_date = input(stroka)
#     return num_date
#
# def answer_false():
#     print('Не верно')
#
# year = input_input('Ввведите год рождения А.С.Пушкина: ')
# while year != '1799':
#     answer_false()
#     year = input_input('Ввведите год рождения А.С.Пушкина: ')
#
# day = input_input('В какой день июня родился Пушкин? ')
# while day != '6':
#     answer_false()
#     day = input_input('В какой день июня родился Пушкин? ')
#
# print('Верно')

# *******************************************************************
# ВАРИАНТ 2
def input_year():
    num_year = input('Ввведите год рождения А.С.Пушкина: ')
    return num_year

def input_day():
    num_day = input('В какой день июня родился А.С.Пушкин? ')
    return num_day

def answer_false():
    print('Не верно')

year = input_year()
while year != '1799':
    answer_false()
    year = input_year()

day = input_day()
while day != '6':
    answer_false()
    day = input_day()

print('Верно')
