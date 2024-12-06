d = {True: 1, False: 2}
del d[True]
print(d)

print(dir(dict))

##### метод index для кортежів
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


