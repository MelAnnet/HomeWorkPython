# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user(name, surname, yearbirth, city, email, phone):
    print(name, surname, yearbirth, city, email, phone)

user(name= 'Anush', surname='Melkonyan', yearbirth=1995, city='Moscow', email = 'ne_skazhu', phone='8-800-555-35-35')