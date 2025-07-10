"""
паттерн Декоратор

"""
from sys import set_int_max_str_digits

# def select(input_func):                         #создали сам декоратор
#     def output_func():
#         print("*************")
#         input_func()
#         print("*************")
#         input_func()
#         print("*************")
#     return output_func()
#
# @select
# def hello():
#     print("Hello world!")

#Вывод :
# *************
# Hello world!
# *************
# Hello world!
# *************



"""
Получение параметров функции в декораторе.
Декоратор может перехватывать передаваемые в функцию аргументы.
"""

#Показной пример
# def check(input_func):              #создаем декоратор
#     def output_func(*args):
#         input_func(*args)
#     return output_func()
#
# @check
# def print_person(name, age):
#     print(f"Имя: {name}, возраст: {age}")
# print(print_person("Илья", 34))

# def check(input_func):
#     def output_func(*args):
#         name = args[0]
#         age = args[1]  # получаем значение второго параметра
#         if age < 0: age = 1  # если возраст отрицательный, изменяем его значение на 1
#         input_func(name, age)  # передаем функции значения для параметров
#
#     return output_func
#
#
# # определение оригинальной функции
# @check
# def print_person(name, age):
#     print(f"Name: {name}  Age: {age}")
#
#
# # вызов оригинальной функции
# print_person("Tom", 38)
# print_person("Bob", -5)

# def check(input_func):              #создаем декоратор
#     def output_func(*args):
#         name = args[0]
#         age = args[1]
#         if age < 0:
#             age = 1
#         input_func(name, age)
#     return output_func
#
# @check
# def print_person(name, age):
#     print(f"Имя: {name}, возраст: {age}")
# print_person("Илья", 34)        #Имя: Илья, возраст: 34
# print_person("Tom", 38)         #Имя: Tom, возраст: 38
# print_person("Bob", -5)              #Имя: Bob, возраст: 1



"""
Получение результата функции
"""

# def check(input_func):
#     def output_func(*args):
#         result = input_func(*args)
#         if result < 0:
#             result = 0
#         return result
#     return output_func
#
# @check
# def sum(a, b):
#     return a + b
#
# result1 = sum(10,10)
# print(result1)                  #20
#
# result2 = sum(10, -100)
# print(result2)                  #0


# import time
# def timer(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print(f"Время выполнения: {end_time - start_time:.4f} секунд")
#         return result
#     return wrapper
#
# @timer
# def long_running_function():
#     time.sleep(2)
#     print("Hello world!")
#
# long_running_function()             #Hello world!
                                      #Время выполнения: 2.000252 секунд


"""
Декоратор для проверки прав доступа
"""

# def requires_permission(permission):
#     def decorator(func):
#         def wrapper():
#             if permission == "admin":
#                 print("Доступ разрешен!")
#                 return func()
#             else:
#                 print("Доступ запрещен!")
#         return wrapper
#     return decorator
#
# @requires_permission("admin")
# def view_admin_panel():
#     print("Добро пожаловать в админ панель!")
# view_admin_panel()                      #Доступ разрешен!
                                        #Добро пожаловать в админ панель!








