# 2) Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def users_data(name, surname, year_of_birth, city, email, telephone_number):
    return print(f'Имя: {name}, Фамилия: {surname}, '
                f'Год рождения: {year_of_birth}, '
                f'Город проживания: {city}, Email: {email}, '
                f'Телефон: {telephone_number}')


users_data(
    name = input("Имя пользователя:"),
    surname = input("Фамилия пользователя:"),
    year_of_birth = int(input("Год рождения:")),
    city = input("Город проживания:"),
    email = input("Email пользователя:"),
    telephone_number = int(input("Номер телефона:")),
)
