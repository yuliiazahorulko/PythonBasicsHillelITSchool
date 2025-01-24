###
# class MyClass:
#     def __init__(self, x):
#         self.x = x
#
#
# obj = MyClass(10)
# obj.y = 20
# print(obj.__dict__)


# ####
# class MyClass:
#     # __slots__ = ['x', 'y']
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# obj = MyClass(10, 20)
# obj.z = 30


# ###
# class MyClass:
#     def __getattr__(self, name):
#         return f"Атрибут '{name}' не знайдено!"
#
#
# obj = MyClass()
# print(obj.x)
#
#
# ###
# class MyClass:
#     def __setattr__(self, name, value):
#         if name == 'x' and not isinstance(value, int):
#             raise ValueError("Атрибут 'x' має бути числом!")
#         super().__setattr__(name, value)  # Виклик стандартного встановлення
#
#
# obj = MyClass()
# obj.x = 10
# obj.x = "текст"
#
#
# ###
# class MyClass:
#     def __delattr__(self, name):
#         print(f"Атрибут '{name}' буде видалено!")
#         super().__delattr__(name)
#
#
# obj = MyClass()
# obj.x = 42
# del obj.x

# ########################################################################################################
# import math
#
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius  # Використовуємо властивість для перевірки даних
#
#     @property
#     def radius(self):
#         return self._radius
#
#     @radius.setter
#     def radius(self, value):
#         if value < 0:
#             raise ValueError("Радіус не може бути від'ємним!")
#         self._radius = value
#
#     @property
#     def area(self):
#         return math.pi * self._radius ** 2
#
#
# circle = Circle(5)
# print(dir(circle))
# print(f"Радіус: {circle.radius}")  # Радіус: 5
# print(f"Площа: {circle.area:.2f}")  # Площа: 78.54
#
# circle.radius = 10
# print(f"Новий радіус: {circle.radius}")  # Новий радіус: 10
# print(f"Нова площа: {circle.area:.2f}")  # Нова площа: 314.16
#
# try:
#     circle.radius = -3
# except ValueError as e:
#     print(e)  # Радіус не може бути від'ємним!


# ########################################################################################################
# Приклад із доступом до атрибута (__get__):
# class Descriptor:
#     def __get__(self, instance, owner):
#         print(f"__get__ викликаний: instance={instance}, owner={owner}")
#         return "Дані з дескриптора"
#
#
# class MyClass:
#     attr = Descriptor()
#
#
# obj = MyClass()
# obj.a = 1
# print(obj.attr)
# obj.attr = 1
# print(obj.attr)


#
# ########################################################################################################
# # Приклад із встановлення атрибута (__set__):
# class Descriptor:
#     def __set__(self, instance, value):
#         print(f"__set__ викликаний: instance={instance}, value={value}")
#
#
# class MyClass:
#     attr = Descriptor()
#
#
# obj = MyClass()
# obj.attr = 42
# print(obj.attr)
#
#
# ########################################################################################################
# Приклад із видалення атрибута (__delete__):
# class Descriptor:
#     def __delete__(self, instance):
#         print(f"__delete__ викликаний: instance={instance}")
#
#
# class MyClass:
#     attr = Descriptor()
#
#
# obj = MyClass()
# del obj.attr
#
#
# ########################################################################################################
# # Демонстрація виклику методів із різними параметрами
# class Descriptor:
#     def __get__(self, instance, owner):
#         print(f"__get__ викликаний: instance={instance}, owner={owner}")
#         return "Значення"
#
#     def __set__(self, instance, value):
#         print(f"__set__ викликаний: instance={instance}, value={value}")
#
#     def __delete__(self, instance):
#         print(f"__delete__ викликаний: instance={instance}")
#
#
# class MyClass:
#     attr = Descriptor()
#
#
# obj = MyClass()
# print(obj.attr)
# obj.attr = 42
# del obj.attr
#
#
#
#
