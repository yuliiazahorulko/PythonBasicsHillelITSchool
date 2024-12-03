##########################################################################################################
# пріорітет операторів
operator = ""
if operator == "+" or "-":
    print("маємо + або -")
else:
    print("маємо не + і не -")



# Приклад 1
result = divmod(10, 3)
print(result)  # Виведе: (3, 1)
# 10 // 3 = 3 (цілочисельне ділення)
# 10 % 3 = 1 (залишок від ділення)

# Приклад 2
result = divmod(25, 4)
print(result)  # Виведе: (6, 1)
# 25 // 4 = 6
# 25 % 4 = 1

# Приклад 3
result = divmod(20, 5)
print(result)  # Виведе: (4, 0)
# 20 // 5 = 4
# 20 % 5 = 0


# додатково
a = 1
b = 2
a, b = b, a
print(a, b)


m, n = [1, 2]
print(m, n)





##########################################################################################################
# methods and functions for list

# methods for list
# 1. append()
# Метод append() додає елемент до кінця списку.
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # [1, 2, 3, 4]

# 2. extend()
# Метод extend() додає всі елементи з іншого ітерабельного об'єкта до списку.
my_list = [1, 2, 3]
my_list.extend([4, 5, 6])
print(my_list)  # [1, 2, 3, 4, 5, 6]

# 3. insert()
# Метод insert() вставляє елемент на вказану позицію.
my_list = [1, 2, 3]
my_list.insert(1, "new")
print(my_list)  # [1, "new", 2, 3]


# 4. remove()
# Метод remove() видаляє перший елемент зі списку, що дорівнює значенню.
my_list = [1, 2, 3, 4]
my_list.remove(3)
print(my_list)  # [1, 2, 4]

# 5. pop()
# Метод pop() видаляє елемент на вказаній позиції (за замовчуванням видаляється останній елемент) і повертає його.
my_list = [1, 2, 3, 4]
popped_item = my_list.pop(1)
print(popped_item)  # 2
print(my_list)  # [1, 3, 4]

# 6. clear()
# Метод clear() видаляє всі елементи з списку.
my_list = [1, 2, 3, 4]
my_list.clear()
print(my_list)  # []


# 7. index()
# Метод index() повертає індекс першого елемента, що дорівнює значенню.
my_list = [1, 2, 3, 4]
index = my_list.index(3)
print(index)  # 2

# 8. count()
# Метод count() повертає кількість елементів у списку, які дорівнюють значенню.
my_list = [1, 2, 3, 1, 1]
count = my_list.count(1)
print(count)  # 3


# 9. sort()
# Метод sort() сортує список на місці.
my_list = [3, 1, 4, 2]
my_list.sort()
print(my_list)  # [1, 2, 3, 4]

# 10. reverse()
# Метод reverse() перевертає список на місці.
my_list = [1, 2, 3, 4]
my_list.reverse()
print(my_list)  # [4, 3, 2, 1]


# 11. copy()
# Метод copy() створює поверхневу копію списку.
my_list = [1, 2, 3]
copied_list = my_list.copy()
print(copied_list)  # [1, 2, 3]


# !!!!!!!!!!!!!!!!!! deepcopy
import copy

original = [1, [2, 3], 4]
deep_copy = copy.deepcopy(original)
copy_default = original.copy()

deep_copy[1][0] = 99
print(original)  # [1, [2, 3], 4] - оригінал не змінений
print(deep_copy) # [1, [99, 3], 4]
print(copy_default) # [1, [2, 3], 4]

original[1][1] = 99
print(original) # [1, [2, 99], 4]
print(deep_copy) # [1, [99, 3], 4]
print(copy_default) # [1, [2, 99], 4]
###### !!!!!!!!!!!


# functions for list
# Порівняємо sort і sorted
# Використання sorted() для створення нового відсортованого списку
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
new_list = sorted(my_list)
print(my_list)
print(new_list)  # Відсортований список

# Використання sort() для сортування на місці
my_list.sort()
print(my_list)  # Список змінено






##########################################################################################################
# match...case
x = 10

match x:
    case 1:
        print("x дорівнює 1")
    case 10:
        print("x дорівнює 10")
    case _:
        print("x має інше значення")


# 1. Використання з кількома варіантами
x = "apple"

match x:
    case "apple":
        print("Це яблуко")
    case "banana":
        print("Це банан")
    case "orange":
        print("Це апельсин")
    case _:
        print("Це інший фрукт")

# 2. Спрощена форма з кількома варіантами в одному case
x = "banana"

match x:
    case "apple" | "orange":
        print("Це яблуко або апельсин")
    case "banana":
        print("Це банан")
    case _:
        print("Це інший фрукт")

# 3. Використання match з умовами
x = 25

match x:
    case n if n < 10:
        print("Число менше 10")
    case n if n < 20:
        print("Число менше 20, але більше або рівне 10")
    case n if n >= 20:
        print("Число більше або рівне 20")

# 4. Використання match для перевірки типу
def check_value(x):
    match x:
        case int():
            print("Це ціле число")
        case str():
            print("Це рядок")
        case float():
            print("Це число з плаваючою крапкою")
        case _:
            print("Це невідомий тип")

check_value(10)
check_value("hello")
check_value(3.14)

# завдання 1
month = int(input("Введіть номер місяця (1-12): "))

match month:
    case 12 | 1 | 2:
        print("Зима")
    case 3 | 4 | 5:
        print("Весна")
    case 6 | 7 | 8:
        print("Літо")
    case 9 | 10 | 11:
        print("Осінь")
    case _:
        print("Невірний номер місяця")
# завдання 2
number = int(input("Введіть число: "))

match number:
    case number if number < 0:
        print("Число від'ємне.")
    case 0:
        print("Число нуль.")
    case number if number > 0:
        print("Число додатнє.")





##########################################################################################################
# for and while
i = 0
while True:
    i += 1
    print(i)


count = 0
is_true = True  # прапор
while is_true:
    count += 1
    print(count)
    if count > 10:
        is_true = False
print("end")

count = 0
while count < 10:
    count += 1
    print(count)

count = 0
while count < 10:
    count += 1
    print(count)
else:
    print("finished")


count = 0
while count < 10:
    count += 1
    print(count)
    if count == 5:
        break
else:
    print("finished")
print("end")

count = 0
while count < 10:
    if count == 2:
        continue
    count += 1
    print(count)
    if count == 5:
        break
else:
    print("finished")
print("end")



#######################################
# Приклад 1: Перебір елементів списку
my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(item)

# Приклад 3: Ітерація по рядку
my_string = "Hello"
for char in my_string:
    print(char)

# Приклад 2: Використання діапазону з range()
for i in range(1, 6):
    print(i)

# Приклад 4: Перебір індексів елементів списку
my_list = ['apple', 'banana', 'cherry']
for index in range(len(my_list)):
    print(f"Index {index}: {my_list[index]}")






##########################################################################################################
# range
# Приклад 1: Створення послідовності від 0 до 4
for i in range(5):
    print(i)
# 0
# 1
# 2
# 3
# 4
# Приклад 2: Вказання початку та кінця
for i in range(2, 6):
    print(i)
# 2
# 3
# 4
# 5
# Приклад 3: Використання кроку
for i in range(1, 10, 2):
    print(i)
# 1
# 3
# 5
# 7
# 9
# Приклад 4: Зворотна послідовність
for i in range(10, 0, -2):
    print(i)
# 10
# 8
# 6
# 4
# 2
# Приклад 5: Перетворення в список
numbers = list(range(5))
print(numbers)
# [0, 1, 2, 3, 4]
# Приклад 6: Обчислення суми чисел
total = sum(range(1, 101))
print(total)
# 5050
# Приклад 7: list comprehesion



##########################################################################################################
# enumerate(iterable, start=0)
# Приклад 1: Ітерація зі списком
fruits = ["яблуко", "банан", "вишня"]
for index, fruit in enumerate(fruits):
    print(f"Індекс {index}: {fruit}")
# Індекс 0: яблуко
# Індекс 1: банан
# Індекс 2: вишня

# Приклад 2: Початковий індекс із start
fruits = ["яблуко", "банан", "вишня"]
for index, fruit in enumerate(fruits, start=1):
    print(f"Елемент {index}: {fruit}")
# Елемент 1: яблуко
# Елемент 2: банан
# Елемент 3: вишня

# !!!!!!
# Приклад 3: З рядком
text = "Python"
for index, char in enumerate(text):
    print(f"Символ '{char}' на позиції {index}")
# Символ 'P' на позиції 0
# Символ 'y' на позиції 1
# Символ 't' на позиції 2
# Символ 'h' на позиції 3
# Символ 'o' на позиції 4
# Символ 'n' на позиції 5

# Приклад 4: Перетворення на список
numbers = [10, 20, 30]
indexed_numbers = list(enumerate(numbers, start=100))
print(indexed_numbers)
# [(100, 10), (101, 20), (102, 30)]

# Приклад 5: Використання з кортежами
data = ("a", "b", "c")
for idx, value in enumerate(data):
    print(f"{idx} -> {value}")
# 0 -> a
# 1 -> b
# 2 -> c
# /!!!!!!!!!!!!

##########################
# завдання
# 1
number = int(input("Введіть число для таблиці множення: "))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
# 2
while True:
    number = int(input("Введіть позитивне число: "))
    if number > 0:
        break
    else:
        print("Будь ласка, введіть позитивне число.")

sum_numbers = sum(range(1, number + 1))
print(f"Сума чисел від 1 до {number}: {sum_numbers}")





##########################################################################################################
# import random
# 1 - random.random()
# Генерує випадкове число з плаваючою крапкою в інтервалі [0.0, 1.0).
print(random.random())  # Наприклад: 0.3743

# 2 - random.randint(a, b)
# Повертає випадкове ціле число в діапазоні [a, b], включно.
print(random.randint(1, 10))  # Наприклад: 7

# 3. random.uniform(a, b)
# Повертає випадкове число з плаваючою крапкою в діапазоні [a, b].
print(random.uniform(1.5, 5.5))  # Наприклад: 3.742

# 4. random.choice(sequence)
# Повертає випадковий елемент із переданої послідовності (list, tuple, string).
fruits = ["яблуко", "банан", "вишня"]
print(random.choice(fruits))  # Наприклад: "вишня"

# 5. random.choices(sequence, k)
# Повертає список із k випадкових елементів із послідовності (з повтореннями).
print(random.choices(fruits, k=2))  # Наприклад: ['яблуко', 'яблуко']

# 6. random.sample(sequence, k)
# Повертає список із k унікальних елементів із послідовності (без повторень).
print(random.sample(fruits, k=2))  # Наприклад: ['вишня', 'яблуко']

# 7. random.shuffle(sequence)
# Перемішує список випадковим чином. Змінює сам список.
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)  # Наприклад: [4, 1, 5, 3, 2]

# 8. random.randrange(start, stop, step)
# Повертає випадкове число з діапазону [start, stop) з кроком step.
print(random.randrange(1, 10, 2))  # Наприклад: 3 (з можливих: 1, 3, 5, 7, 9)

# 9. random.seed(a=None)
# Ініціалізує генератор випадкових чисел певним значенням. Це дозволяє отримувати
# однакові результати при кожному запуску програми.
random.seed(42)
print(random.random())  # Завжди поверне те саме числ


# Завдання 1: Гра "Вгадай число"
import random

secret_number = random.randint(1, 10)

guess = int(input("Вгадайте число від 1 до 10: "))

if guess == secret_number:
    print("Вітаю! Ви вгадали!")
else:
    print(f"Неправильно. Загадане число було: {secret_number}")


# Завдання 2: Генерація випадкового пароля
import random
import string

characters = string.ascii_letters + string.digits

password = ''.join(random.choices(characters, k=8))

print(f"Ваш випадковий пароль: {password}")

# Завдання 3: Перемішування списку студентів
import random

students = ["Аліна", "Богдан", "Вікторія", "Дмитро", "Євгенія"]

random.shuffle(students)

print("Студенти у випадковому порядку:")
print(students)

# завдання 4
import random

random_list_1 = [random.randint(1, 100) for _ in range(random.randint(5, 15))]
second_element = random_list_1[1]
middle_element = random_list_1[len(random_list_1) // 2]
last_element = random_list_1[-1]
new_list_1 = [second_element, middle_element, last_element]

print("Завдання 1")
print("Початковий список:", random_list_1)
print("Новий список:", new_list_1)



# завдання 5
random_list_2 = [random.randint(10, 99) for _ in range(random.randint(6, 12))]
mid_index = len(random_list_2) // 2
first_half_sum = sum(random_list_2[:mid_index])
second_half_sum = sum(random_list_2[-mid_index:])
max_element = max(random_list_2)
min_element = min(random_list_2)
new_list_2 = [first_half_sum + second_half_sum, max_element, min_element]

print("\nЗавдання 2")
print("Початковий список:", random_list_2)
print("Новий список:", new_list_2)


# 6
random_list_3 = [random.randint(1, 100) for _ in range(random.randint(4, 8))]
first_two_elements = random_list_3[:2]
second_last_element = random_list_3[-2]
last_two_sum = sum(random_list_3[-2:])
new_list_3 = first_two_elements + [second_last_element, last_two_sum]

print("\nЗавдання 3")
print("Початковий список:", random_list_3)
print("Новий список:", new_list_3)

##########################################################################################################
# list comprehension

# Приклад 1: Простий List comprehension
# Створимо список квадратів чисел від 1 до 5:
squares = [x ** 2 for x in range(1, 6)]
print(squares)
# [1, 4, 9, 16, 25]

# Приклад 2: List comprehension з умовою
# Тепер створимо список тільки парних чисел з діапазону від 1 до 10:
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(even_numbers)
# [2, 4, 6, 8, 10]

# Можливості з використанням if-else:
# Можна використовувати умовні вирази для створення різних значень на основі умови:
numbers = [1, 2, 3, 4, 5]
squared_or_cubed = [x ** 2 if x % 2 == 0 else x ** 3 for x in numbers]
print(squared_or_cubed)
# [1, 4, 27, 16, 125]


# задачі
# Задача 1: Перетворення списку чисел у їх квадрати
numbers = [1, 2, 3, 4, 5]

squares = [x ** 2 for x in numbers]

print(squares)
# [1, 4, 9, 16, 25]
# Задача 2: Фільтрація парних чисел
numbers = list(range(1, 21))

even_numbers = [x for x in numbers if x % 2 == 0]

print(even_numbers)
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# Задача 3: Сума елементів на непарних індексах списку
numbers = [1, 2, 3, 4, 5]

sum_odd_index_elements = sum(numbers[i] for i in range(1, len(numbers), 2))

print(sum_odd_index_elements)
# 6
# Задача 4: Комбінування умов і операцій
numbers = [1, 2, 3, 4, 5]

squared_or_cubed = [x ** 2 if x % 2 == 0 else x ** 3 for x in numbers]

print(squared_or_cubed)
# [1, 4, 27, 16, 125]
