# 3) Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(first_num, second_num, third_num):
    print(f'Сумма двух наибольших элементов = '
          f'{(first_num + second_num + third_num) - min(first_num, second_num, third_num)}')


my_func(
    int(input('Первое число:')),
    int(input('Второе число:')),
    int(input('Третье число:')),
)
