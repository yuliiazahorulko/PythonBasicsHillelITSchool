# # multilple exceptions
#
# try:
#     value = int(input("Введіть число: "))
#     result = 10 / value
# except ValueError:
#     print("Помилка: Ви повинні ввести число!")
# except ZeroDivisionError:
#     print("Помилка: Ділення на нуль неможливе!")

# ###
# 0
# try:
#     value = int(input("Введіть число: "))
#     result = 10 / value
# except Exception as e:
#     print(f"Помилка: {e}")

# ###
# try:
#     value = int(input("Введіть число: "))
#     result = 10 / value
# except Exception as e:
#     print(f"Сталася помилка: {e}")
#
# ######
#
#
# class NegativeNumberError(Exception):
#     pass
#
#
# def square_root(number):
#     if number < 0:
#         raise NegativeNumberError("Квадратний корінь від від'ємного числа неможливий!")
#     return number ** 0.5
#
# try:
#     result = square_root(-4)
# except NegativeNumberError as e:
#     print(f"Помилка: {e}")

# #####
#
# try:
#     raise ValueError("Помилка!")
# except ValueError:
#     print("Обробка помилки...")
#     raise  # Підняти ту саму помилку
#
#
# ## assertion
#
# x = 10
# assert x > 0, "Значення x повинно бути додатним"
#
#
# #####
#
# def process_number(number):
#     assert isinstance(number, int), "Вхідні дані повинні бути цілим числом"
#     if number < 0:
#         raise ValueError("Число не може бути від'ємним")
#     return number ** 2
#
# print(process_number(5))   # 25
# print(process_number(-5))  # ValueError: Число не може бути від'ємним
# print(process_number("5")) # AssertionError: Вхідні дані повинні бути цілим числом
#
#
# #####
# # python -O script.py
# # Приклад використання assert
# def check_positive(x):
#     assert x > 0, "Число має бути додатним"
#     return x
#
# # Запуск без оптимізації
# check_positive(-5)  # AssertionError: Число має бути додатним
#
# # Запуск із флагом -O
# # python -O script.py
# check_positive(-5)  # НЕ викличе помилку, оскільки assert ігнорується

#
# def vadidate_age():
#     try:
#         print(1/0)
#     except:
#         print("exception")
#         raise ZeroDivisionError()
#
#
# def another():
#     try:
#         print(1)
#         vadidate_age()
#         print(2)
#     except:
#         print("Another")
#
#
# another()

# import time
#
#
# text = """Beautiful is better than ugly.
#     Explicit is better than implicit.
#     Simple is better than complex.
#     Complex is better than complicated.
#     Flat is better than nested.
#     Sparse is better than dense.
#     Readability counts.
#     Special cases aren't special enough to break the rules.
#     Although practicality beats purity.
#     Errors should never pass silently.
#     Unless explicitly silenced.
#     In the face of ambiguity, refuse the temptation to guess.
#     There should be one-- and preferably only one --obvious way to do it.
#     Although that way may not be obvious at first unless you're Dutch.
#     Now is better than never.
#     Although never is often better than *right* now.
#     If the implementation is hard to explain, it's a bad idea.
#     If the implementation is easy to explain, it may be a good idea.
#     Namespaces are one honking great idea -- let's do more of those!
#     """
# with open('zen.txt', 'w+') as f:
#     f.write(text)
#
#
# try:
#     f = open('zen.txt')
#     while True: # звичайний спосіб читати файли
#         line = f.readline()
#         if len(line) == 0:
#             break
#         print(line, end='')
#         time.sleep(2) # тайм аут
# except KeyboardInterrupt:
#     print('!! Ви скасували читання файлу.')
# finally:
#     f.close()
#     print('Очищення: Закриття файлу')


# 1. Напишіть функцію, яка приймає два параметри і намагається їх додати.
# Якщо один з параметрів не є числом (наприклад, рядок), вивести повідомлення
# про помилку.

# def add_numbers(a, b):
#     try:
#         return a + b
#     except TypeError:
#         return "Type Error"
#
#
# print(add_numbers(5,8))
# print(add_numbers(9,"i"))

# 2. Напишіть програму, яка приймає словник і ключ. Потрібно повернути значення,
# яке відповідає ключу, або вивести повідомлення, якщо ключ не знайдений.

# def value_dictionary(dictionary, key):
#     try:
#         # assert key in dictionary.keys(), "no key in dictionary"
#         if not key in dictionary.keys():
#             raise KeyError("Custom text for KetError!!!")
#         value = dictionary[key]
#
#         print(value)
#     except KeyError as e:
#         print("Error - ", e)
#     # value = dictionary[key]
#     # print(value)
#
#
# value_dictionary({"b": 1, "c": 5}, "b")







# 3. Напишіть програму, яка приймає ім'я файлу і намагається відкрити його. Якщо
# файл не знайдений, вивести відповідне повідомлення.



# 4. Напишіть програму, яка приймає рядок і намагається перетворити його на ціле
# число. Якщо рядок не можна перетворити, вивести повідомлення про помилку.


def convert_int(string):
    try:
        num = int(string)
        print(num)
    except ValueError as e:
        print(f"Error!! - {e}")


convert_int("abc")

# 5. Напишіть програму, яка приймає два параметри: число для ділення і список.
# Потрібно поділити кожен елемент списку на задане число. Якщо в списку є елемент,
# який не можна поділити (наприклад, рядок), або число для ділення є нулем, вивести
# відповідне повідомлення про помилку.


# def divide_by_custom_number(number, lst):
#     result = []
#     try:
#         for item in lst:
#             result.append(item / number)
#     except ZeroDivisionError as e:
#         print(f"Cannot divide by zero", e)
#     except TypeError as e:
#         print(e)
#     finally:
#         print(result)
#
#
# divide_by_custom_number(0, [1, 2, 3, 4, "5", 6])
#
