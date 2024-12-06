d = {True: 1, False: 2}
del d[True]
print(d)

print(dir(dict))

##### метод index для корт# +, -, *, \, and, or, not, //, %, **, (), ==, !==, >, <




text01 = 'Це рядок'
text02 = "Це також рядок"
text03 = '''Багаторядковий
рядок'''
text04 = """Ще один
багаторядковий рядок"""
################################

text = "Python"
print(text[0])  # 'P'
print(text[-1])  # 'n' (від'ємна індексація)

text = "Hello"
# text[0] = 'h'  # Помилка: TypeError

text = "Hello"
print(len(text))  # 5
###############################
text1 = "Hello"
text2 = "World"
result = text1 + " " + text2
print(result)  # "Hello World"

text3 = "Hi"
result = text * 3
print(result)  # "HiHiHi"

text = "Hello, World"
print("World" in text)  # True

#################################
# This prints out "Hello, John!“
name = "John"
print("Hello, %s!" % name)

name = "John"
age = 30
print("Name: %s, Age: %d" % (name, age))

# This prints out "John is 23 years old. Your salary is 999.990 $"
name = "John"
age = 23
salary = 999.99
print("%s is %d years old. Your salary is %.3f $" % (name, age, salary))

################

# default(implicit) order
default_order = "{}, {} and {}".format('John', 'Bill', 'Sean')
# order using positional argument
positional_order = "{1}, {0} and {2}".format('John', 'Bill', 'Sean')
# order using keyword argument
keyword_order = "{s}, {b} and {j}".format(j='John', b='Bill', s='Sean')

# formatting integers
print("Binary representation of {0} is {0:b}".format(12))
# => 'Binary representation of 12 is 1100'

# formatting floats
print("Exponent representation: {0:e}".format(1566.345))
# => 'Exponent representation: 1.566345e+03'

# round off
print("One third is: {0:.3f}".format(1/3))
# => 'One third is: 0.333'

############

print(dir(str))



###########

print("eeee".index("e"))




############### задачі
# string
# 1
# Отримуємо вхідний рядок
sentence = input("Введіть речення: ")

# Розділяємо на слова
words = sentence.split()

# Виводимо список слів
print("Список слів:", words)
# 2
# Отримуємо вхідний рядок
string = input("Введіть рядок: ")

# Перевірка, чи починається з цифри
if string and string[0].isdigit():
    print("Рядок починається з цифри.")
else:
    print("Рядок не починається з цифри.")
# 3
# Отримуємо вхідний рядок
string = input("Введіть рядок: ")

# Перевірка регістру символів
if string.islower():
    print("Усі символи рядка є малими.")
elif string.isupper():
    print("Усі символи рядка є великими.")
else:
    print("Символи рядка змішані.")
# 4
# Отримуємо вхідний рядок
sentence = input("Введіть речення: ")

# Розділяємо на слова та капіталізуємо кожне слово
capitalized_words = [word.capitalize() for word in sentence.split()]

# Об'єднуємо слова назад у речення
result = " ".join(capitalized_words)

print("Речення з капіталізованими словами:", result)
# 5
import string

# Отримуємо вхідний рядок
string_input = input("Введіть рядок: ")

# Перевірка на наявність пробілів чи пунктуації
contains_punctuation = any(char in string.punctuation for char in string_input)
contains_space = " " in string_input

if contains_punctuation or contains_space:
    print("Рядок містить пробіли або знаки пунктуації.")
else:
    print("Рядок не містить пробілів і знаків пунктуації.")
# 6
# Отримуємо вхідний рядок
string = input("Введіть рядок: ")

# Підрахунок символів "_"
underscore_count = string.count("_")

print(f"Кількість символів '_': {underscore_count}")
# 7
import keyword

# Отримуємо вхідний рядок
word = input("Введіть слово: ")

# Перевірка, чи є слово зарезервованим
if word in keyword.kwlist:
    print(f"'{word}' є зарезервованим словом у Python.")
else:
    print(f"'{word}' не є зарезервованим словом у Python.")
# 8
import string

# Отримуємо вхідний рядок
sentence = input("Введіть рядок: ")

# Таблиця видалення пунктуації
translator = str.maketrans("", "", string.punctuation)

# Видалення пунктуації
clean_sentence = sentence.translate(translator)

print("Рядок без знаків пунктуації:", clean_sentence)






#####
# for and while
# 1 for
numbers = [1, 2, 3, 4, 5]
total = 0

for num in numbers:
    total += num

print(total)  # Виведе: 15
# 2 while
n = 5
factorial = 1

while n > 0:
    factorial *= n
    n -= 1

print(factorial)  # Виведе: 120
# 3
text = "hello world"
vowels = "aeiou"
count = 0

for char in text:
    if char in vowels:
        count += 1

print(count)  # Виведе: 3
# 4
number = 50

while number % 7 != 0:
    number += 1

print(number)  # Виведе: 56


##### list comprehension
# 1
squares = [x**2 for x in range(1, 11)]
print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# 2
even_numbers = [x for x in range(1, 21) if x % 2 == 0]
print(even_numbers)  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# 3
words = ["apple", "banana", "cherry"]
lengths = [len(word) for word in words]
print(lengths)  # [5, 6, 6]
# 4
multiples_of_three = [x for x in range(1, 31) if x % 3 == 0]
print(multiples_of_three)  # [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
# 5
numbers = [1, 2, 3, 4, 5]
string_numbers = [str(num) for num in numbers]
print(string_numbers)  # ['1', '2', '3', '4', '5']
# 6
words = ["hello", "world", "python"]
first_letters = [word[0] for word in words]
print(first_letters)  # ['h', 'w', 'p']
# 7
words = ["hello", "world", "python"]
reversed_words = [word[::-1] for word in words]
print(reversed_words)  # ['olleh', 'dlrow', 'nohtyp']

ежів
# Приклади використання
# Без start_index та end_index (пошук у всьому кортежі):
t = (1, 2, 3, 4, 2)
print(t.index(2))  # 1 (перший індекс, де зустрічається 2)

# З початковим індексом (start_index):
t = (1, 2, 3, 4, 2)
print(t.index(2, 2))  # 4 (пошук починається з індексу 2)

# З діапазоном пошуку (start_index і end_index):
t = (1, 2, 3, 4, 2)
print(t.index(2, 1, 4))  # 1 (пошук у межах індексів 1–3)

# Коли елемент не знайдено: Якщо елемент відсутній у вказаному діапазоні, виникає помилка ValueError.
t = (1, 2, 3, 4)
print(t.index(5))  # ValueError: tuple.index(x): x not in tuple
print(t.index(2, 2, 4))  # ValueError




##### методи словників
# Метод get() з дефолтним значенням:
my_dict = {"name": "Alice", "age": 25}
print(my_dict.get("city", "Unknown"))  # Вивід: "Unknown"

# Метод keys() для отримання всіх ключів:
my_dict = {"name": "Alice", "age": 25}
print(my_dict.keys())  # Вивід: dict_keys(['name', 'age'])

# Метод values() для отримання всіх значень:
my_dict = {"name": "Alice", "age": 25}
print(my_dict.values())  # Вивід: dict_values(['Alice', 25])

# Метод items() для отримання пар ключ-значення:
my_dict = {"name": "Alice", "age": 25}
print(my_dict.items())  # Вивід: dict_items([('name', 'Alice'), ('age', 25)])

# Метод update() для додавання нових елементів:
my_dict = {"name": "Alice"}
my_dict.update({"age": 25, "city": "New York"})
print(my_dict)  # Вивід: {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Метод setdefault() для додавання ключа зі значенням:
my_dict = {"name": "Alice"}
my_dict.setdefault("age", 25)  # Якщо "age" немає, додається з значенням 25
print(my_dict)  # Вивід: {'name': 'Alice', 'age': 25}

# Метод fromkeys() для створення словника:
keys = ["name", "age"]
my_dict = dict.fromkeys(keys, "unknown")  # Створення словника
print(my_dict)  # Вивід: {'name': 'unknown', 'age': 'unknown'}

# Метод copy() для копії словника:
my_dict = {"name": "Alice", "age": 25}
my_dict_copy = my_dict.copy()  # Копія словника
print(my_dict_copy)  # Вивід: {'name': 'Alice', 'age': 25}

# Метод pop() з дефолтним значенням:
my_dict = {"name": "Alice", "age": 25}
print(my_dict.pop("city", "Not Found"))  # Вивід: "Not Found"

# Метод popitem() для видалення пари ключ-значення:
my_dict = {"name": "Alice", "age": 25}
popped_item = my_dict.popitem()  # Видаляє останній елемент
print(popped_item)  # Вивід: ('age', 25)

# Метод clear() для очищення словника:
my_dict = {"name": "Alice", "age": 25}
my_dict.clear()  # Очищає словник
print(my_dict)  # Вивід: {}


# функції словників
# len()
# Функція len() повертає кількість елементів у словнику, тобто кількість пар ключ-значення.
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print(len(my_dict))  # Вивід: 3
# 2. del
# Оператор del використовується для видалення пари ключ-значення за певним ключем або для видалення всього словника.
my_dict = {"name": "Alice", "age": 25}
del my_dict["age"]
print(my_dict)  # Вивід: {'name': 'Alice'}
# # Для видалення всього словника
del my_dict
# Тепер my_dict не існує
# 3. dict()
# Функція dict() використовується для створення нового словника. Можна передати різні типи даних для ініціалізації.
# Створення словника з пари кортежів
my_dict = dict([("name", "Alice"), ("age", 25)])
print(my_dict)  # Вивід: {'name': 'Alice', 'age': 25}
#
# Створення словника за допомогою ключів та значень
my_dict = dict(name="Alice", age=25)
print(my_dict)  # Вивід: {'name': 'Alice', 'age': 25}
# 4. sorted()
# Функція sorted() дозволяє відсортувати ключі або значення словника за певним критерієм.
my_dict = {"name": "Alice", "age": 25, "city": "New York"}

# Сортування ключів
sorted_keys = sorted(my_dict)
print(sorted_keys)  # Вивід: ['age', 'city', 'name']

# Сортування значень
sorted_values = sorted(my_dict.values())
print(sorted_values)  # Вивід: ['Alice', 25, 'New York']
# 5. all()
# Функція all() повертає True, якщо всі елементи ітерабельного об'єкта (включаючи ключі та значення словника) є істинними.
my_dict = {"name": "Alice", "age": 25}

# Перевірка, чи всі значення є істинними
print(all(my_dict))  # Вивід: True
# 6. any()
# Функція any() повертає True, якщо хоча б один елемент ітерабельного об'єкта є істинним.
my_dict = {"name": "Alice", "age": 0}

# Перевірка, чи є хоча б один істинний елемент
print(any(my_dict))  # Вивід: True, оскільки "name" є істинним
# 7. zip()
# Функція zip() може використовуватися для поєднання двох списків (наприклад, ключів і значень) у словник.
keys = ["name", "age", "city"]
values = ["Alice", 25, "New York"]

# Перетворення списків у словник
my_dict = dict(zip(keys, values))
print(my_dict)  # Вивід: {'name': 'Alice', 'age': 25, 'city': 'New York'}
# 8. map()
# Функція map() може бути використана для застосування функції до кожного елемента словника, якщо ітерація проводиться через значення.
my_dict = {"name": "Alice", "age": 25}

# Збільшення всіх значень на 1
updated_dict = dict(map(lambda item: (item[0], item[1] + 1) if isinstance(item[1], int) else item, my_dict.items()))
print(updated_dict)  # Вивід: {'name': 'Alice', 'age': 26}
# 9. filter()
# Функція filter() використовується для фільтрації елементів словника за певними умовами.
my_dict = {"name": "Alice", "age": 25, "city": "New York"}

# Фільтрація, щоб залишити лише числові значення
filtered_dict = dict(filter(lambda item: isinstance(item[1], int), my_dict.items()))
print(filtered_dict)  # Вивід: {'age': 25}
# 10. getattr() і setattr() (для класів, що використовують словники)
# Ці функції використовуються для отримання або встановлення атрибутів класу, але вони можуть бути корисними для роботи з об'єктами, які використовують словники.
class MyClass:
    def __init__(self):
        self.my_dict = {"name": "Alice", "age": 25}

# Використання getattr для отримання значення
obj = MyClass()
print(getattr(obj, "my_dict", "Not Found"))  # Вивід: {'name': 'Alice', 'age': 25}

# Використання setattr для зміни значення
setattr(obj, "my_dict", {"city": "New York"})
print(obj.my_dict)  # Вивід: {'city': 'New York'}




### OrderedDict
from collections import OrderedDict

# Створення OrderedDict
od = OrderedDict([('apple', 3), ('banana', 2), ('cherry', 5)])
print(od)  # Вивід: OrderedDict([('apple', 3), ('banana', 2), ('cherry', 5)])

# Переміщення елементу в кінець
od.move_to_end('banana')
print(od)  # Вивід: OrderedDict([('apple', 3), ('cherry', 5), ('banana', 2)])

# Переміщення елементу на початок
od.move_to_end('cherry', last=False)
print(od)  # Вивід: OrderedDict([('cherry', 5), ('apple', 3), ('banana', 2)])

# Видалення і повернення останнього елемента
item = od.popitem()
print(item)  # Вивід: ('banana', 2)
print(od)  # Вивід: OrderedDict([('cherry', 5), ('apple', 3)])

# Очищення OrderedDict
od.clear()
print(od)  # Вивід: OrderedDict()

# Створення зворотного порядку
od = OrderedDict([('apple', 3), ('banana', 2), ('cherry', 5)])
print(list(reversed(od)))  # Вивід: [('cherry', 5), ('banana', 2), ('apple', 3)]





### defaultdict
# Приклад з KeyError в звичайному словнику:

d = {'apple': 1, 'banana': 2}
print(d['cherry'])  # Викине KeyError

# Приклад з defaultdict:

from collections import defaultdict

d = defaultdict(int)
print(d['cherry'])  # Поверне 0, оскільки значення за замовчуванням - це int, а int() дає 0


# Приклади використання defaultdict
# 1. Лічильник елементів (сумування)

from collections import defaultdict

words = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
word_count = defaultdict(int)

for word in words:
    word_count[word] += 1

print(word_count)  # Вивід: defaultdict(<class 'int'>, {'apple': 2, 'banana': 3, 'orange': 1})



### або!!!!!!

from collections import Counter
c = Counter(['a', 'b', 'c', 'a', 'a', 'b'])
print(c)  # Counter({'a': 3, 'b': 2, 'c': 1})


# 2. Групування елементів (списки)

from collections import defaultdict

pairs = [('a', 1), ('b', 2), ('a', 3), ('b', 4), ('c', 5)]
grouped = defaultdict(list)

for key, value in pairs:
    grouped[key].append(value)

print(grouped)  # Вивід: defaultdict(<class 'list'>, {'a': [1, 3], 'b': [2, 4], 'c': [5]})

# 3. Збір елементів у множини (унікальні значення)

from collections import defaultdict

pairs = [('a', 1), ('b', 2), ('a', 3), ('b', 2), ('c', 5)]
grouped_sets = defaultdict(set)

for key, value in pairs:
    grouped_sets[key].add(value)

print(grouped_sets)  # Вивід: defaultdict(<class 'set'>, {'a': {1, 3}, 'b': {2}, 'c': {5}



#### namedtuple
# Приклад з використанням в реальних задачах
# 1. Представлення координат

from collections import namedtuple

# Створення типу для географічної точки
Location = namedtuple('Location', ['latitude', 'longitude'])

# Створення координат
loc = Location(48.8566, 2.3522)  # Париж
print(loc.latitude)   # Виведе: 48.8566
print(loc.longitude)  # Виведе: 2.3522

# 2. Обробка даних про студентів

from collections import namedtuple

# Створення типу для студента
Student = namedtuple('Student', ['name', 'age', 'grade'])

# Створення екземплярів
student1 = Student('John', 21, 'A')
student2 = Student('Jane', 22, 'B')

# Доступ до атрибутів
print(student1.name)   # Виведе: John
print(student2.grade)  # Виведе: B


