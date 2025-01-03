# ### сортування бульбашкою
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         # Оптимізація: перевіряємо, чи був обмін
#         swapped = False
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                 swapped = True
#         # Якщо не було обмінів, масив уже відсортований
#         if not swapped:
#             break
#     return arr
#
# # Приклад використання
# arr = [64, 34, 25, 12, 22, 11, 90]
# sorted_arr = bubble_sort(arr)
# print("Відсортований масив:", sorted_arr)
#
#
# ### лінійний пошук
# def linear_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i  # Повертає індекс знайденого елемента
#     return -1  # Якщо елемент не знайдено
#
# # Приклад використання
# arr = [10, 23, 45, 70, 11, 15]
# target = 70
# result = linear_search(arr, target)
# if result != -1:
#     print(f"Елемент знайдено на індексі: {result}")
# else:
#     print("Елемент не знайдено")
#
#
# ### бінарний пошук
# def binary_search(arr, target):
#     left, right = 0, len(arr) - 1
#
#     while left <= right:
#         mid = (left + right) // 2  # Знаходимо середину
#         if arr[mid] == target:
#             return mid  # Повертаємо індекс, якщо елемент знайдено
#         elif arr[mid] < target:
#             left = mid + 1  # Шуканий елемент у правій частині
#         else:
#             right = mid - 1  # Шуканий елемент у лівій частині
#
#     return -1  # Якщо елемент не знайдено
#
# # Приклад використання
# arr = [1, 3, 5, 7, 9, 11, 13, 15]
# target = 7
# result = binary_search(arr, target)
# if result != -1:
#     print(f"Елемент знайдено на індексі: {result}")
# else:
#     print("Елемент не знайдено")
#
#
# ### Реалізація (рекурсивний підхід)
# def binary_search_recursive(arr, target, left, right):
#     if left > right:
#         return -1  # База рекурсії: елемент не знайдено
#
#     mid = (left + right) // 2  # Знаходимо середину
#     if arr[mid] == target:
#         return mid  # Повертаємо індекс, якщо елемент знайдено
#     elif arr[mid] < target:
#         return binary_search_recursive(arr, target, mid + 1, right)  # У правій частині
#     else:
#         return binary_search_recursive(arr, target, left, mid - 1)  # У лівій частині
#
# # Приклад використання
# arr = [1, 3, 5, 7, 9, 11, 13, 15]
# target = 7
# result = binary_search_recursive(arr, target, 0, len(arr) - 1)
# if result != -1:
#     print(f"Елемент знайдено на індексі: {result}")
# else:
#     print("Елемент не знайдено")
#
#
####### робота з файлами
#
# file_one = open("a.txt","w")
#
# file_one.write("Hello world")
# file_one.write("Hello world")
# file_one.write("Hello world")
#
# file_one.close()
#
# ####
#
# file_one = open("a.txt","w")
# file_one.writelines("Hello world\n")  # \n - Перехід вказівника на новий рядок
# file_one.writelines("\t\tHello world\n")  # \t - Табуляція
# file_one.writelines("Hello world\n")
# file_one.close()
#
# ####
#
# #Додамо у файл елементи списку
# students_list = ["Olga","Sergiy","Petr","Lidia"]
# file_one = open("Students.txt","w")
# for i in range(len(students_list)):
#     file_one.write(f'{i+1})  {students_list[i]}\n')
# file_one.close()
#
# ####
#
# file_one = open("Students.txt","w")
# for i, st in enumerate(students_list, 10):
#     file_one.write(f'{i})  {st}\n')
# file_one.close()
#
# ####
#
# # Ми можемо перетворити список у рядок. Тоді у файлі він відображатиметься схожим на список
# students_list = ["Olga","Sergiy","Petr","Lidia"]
# file_one = open("Students2.txt","w")
# file_one.write(str(students_list))
# file_one.close()
#

####
#
# import codecs
#
#
# data = "unknow codec text"
# handle = codecs.open('some.txt', "w", 'utf-8')
# handle.write(str(data))
# handle.close()
#
#
# ####
#
# with open("example.txt", "w") as file:
#     file.write("Це перший запис у файлі.\n")
#     file.write("Це другий запис у файлі.\n")
#
#
# ###
#
# with open("example.txt", "r") as file:
#     for line in file:
#         print(line.strip())


####
# #
# class Person:
#     def __init__(self, name, age):
#         self.__name = name  # Приватний атрибут
#         self.__age = age    # Приватний атрибут
#
#     def get_name(self):  # Гетер для доступу до name
#         return self.__name
#
#     def set_age(self, age):  # Сетер для зміни age
#         if age > 0:
#             self.__age = age
#
#     def get_age(self):  # Гетер для доступу до age
#         return self.__age
#
#
# # Створюємо об'єкт
# person = Person("Alice", 25)
#
# # Доступ до приватних атрибутів через публічні методи
# print(person.get_name())  # Виведе: Alice
# person.set_age(30)  # Змінюємо вік через сетер
# print(person.get_age())  # Виведе: 30
#
# # Прямий доступ до __name або __age викличе помилку
# person.__name = 35  # Помилка: 'Person' object has no attribute '__name'
# print(person.get_age())
# person._Person__name = "Test"
# print(person._Person__name)
