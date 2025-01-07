class Example:
    apple = 1

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, {self.name}!"

# Створюємо екземпляр класу
obj = Example("Anna", 25)

# 1. Використання __dict__
print("Атрибути через __dict__:", obj.__dict__)

# 2. Використання vars()
print("Атрибути через vars():", vars(obj))

# 3. Використання dir()
all_attributes = dir(obj)
print("Усі доступні атрибути через dir():", all_attributes)

# Фільтрація атрибутів екземпляра (без методів і спеціальних атрибутів)
filtered_attributes = [attr for attr in all_attributes if not callable(getattr(obj, attr)) and not attr.startswith("__")]
print("Атрибути екземпляра після фільтрації:", filtered_attributes)

# Атрибути через __dict__: {'name': 'Anna', 'age': 25}
# Атрибути через vars(): {'name': 'Anna', 'age': 25}
# Усі доступні атрибути через dir(): ['__class__', '__delattr__', '__dict__', ... , 'age', 'greet', 'name']
# Атрибути екземпляра після фільтрації: ['age', 'name']


# 1. getattr(obj, attr)
# Функція getattr() отримує значення атрибуту attr у об'єкта obj.
#
# Наприклад, якщо у нас є obj.name, то getattr(obj, "name") поверне "Anna" (значення атрибуту name).
# 2. callable()
# Функція callable() перевіряє, чи можна викликати переданий їй об'єкт як функцію чи метод.
#
# Якщо об'єкт можна викликати (наприклад, це функція або метод), вона повертає True.
# Якщо об'єкт не можна викликати (наприклад, це число, рядок або будь-яке інше значення), вона повертає False.
# 3. not callable(...)
# Додаючи not, ми перевіряємо, чи є об'єкт невикликаємим. Тобто, якщо це не метод і не функція, вираз поверне True.


# class Singleton:
#     _instance = None  # Зберігає єдиний екземпляр класу
#
#     def __new__(cls, *args, **kwargs):
#         if cls._instance is None:  # Перевірка, чи вже створено екземпляр
#             cls._instance = super().__new__(cls)  # Створення нового екземпляра
#         return cls._instance
#
#     def __init__(self, value):
#         self.value = value  # Ініціалізація атрибуту
#
# # Створення екземплярів
# obj1 = Singleton("First Instance")
# obj2 = Singleton("Second Instance")
#
# # Перевірка
# print(obj1 is obj2)  # True - обидва посилаються на один об'єкт
# print(obj1.value)  # "Second Instance"
# print(obj2.value)  # "Second Instance"
#

