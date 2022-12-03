# 1) Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def devision(first_num, second_num):
    try:
        return first_num / second_num
    except ZeroDivisionError:
        return 'Делить на 0 нельзя'


print(devision(int(input('Первое число:')), int(input('Второе число:'))))
