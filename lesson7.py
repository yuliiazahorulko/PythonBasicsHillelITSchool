print(dir(set))

print(dir(frozenset))
set_example = {1, 2, 3, 4, 4, 4, 2}
print(set_example)


### задачі на теми set frozenset з рішеннями
# 1
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# Створюємо множини
set1 = set(list1)
set2 = set(list2)

# Симетрична різниця
result = set1.symmetric_difference(set2)
print(result)  # Виведе: {1, 2, 3, 6, 7, 8}


# 2
set1 = {1, 2, 3, 4}
set2 = {2, 3}

# Перевірка на підмножину
print(set2.issubset(set1))  # Виведе: True
print(set1.issubset(set2))  # Виведе: False


# 3
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Об'єднання двох наборів
result = set1 | set2
print(result)  # Виведе: {1, 2, 3, 4, 5}


# 4
set1 = {1, 2, 3, 4}
set2 = {5, 6, 7, 8}

# Перевірка на спільні елементи
print(set1 & set2)  # Виведе: set()


# 5
frozenset1 = frozenset([1, 2, 3])
frozenset2 = frozenset([4, 5, 6])

# Створюємо множину з frozenset
set_of_frozensets = {frozenset1, frozenset2}
print(set_of_frozensets)  # Виведе: {frozenset({1, 2, 3}), frozenset({4, 5, 6})}

# Спробуємо додати звичайну множину - це не буде працювати
# set_of_frozensets.add({7, 8})  # TypeError: unhashable type: 'set'


# 6
list1 = [1, 2, 3, 4]
list2 = [4, 3, 2, 1]

# Створюємо frozenset
frozenset1 = frozenset(list1)
frozenset2 = frozenset(list2)

# Перевіряємо на рівність
print(frozenset1 == frozenset2)  # Виведе: True


# 7
set1 = {1, 2, 3}

# Додаємо елемент
set1.add(4)
print(set1)  # Виведе: {1, 2, 3, 4}

# Спробуємо додати вже існуючий елемент
set1.add(3)
print(set1)  # Виведе: {1, 2, 3, 4} (елемент не змінюється)


# 8
set1 = {1, 2, 3, 4, 5}

# Видаляємо елемент
set1.remove(3)
print(set1)  # Виведе: {1, 2, 4, 5}

# Спробуємо видалити елемент, якого немає - викликає помилку
# set1.remove(6)  # KeyError: 6


# 9
numbers = [1, 2, 2, 3, 4, 4, 5]

# Перетворюємо список в множину для видалення дублікатів
unique_numbers = set(numbers)
print(unique_numbers)  # Виведе: {1, 2, 3, 4, 5}


# 10
numbers = [1, 2, 3, 3, 4, 5]

# Якщо кількість елементів в множині дорівнює кількості елементів у списку, то всі елементи унікальні
if len(numbers) == len(set(numbers)):
    print("Усі елементи унікальні")
else:
    print("Є дублікати")

 ####################################

 # arg and kwarg

 def mixed_function(arg1, *args, kwarg1=None, **kwargs):
    print(f"arg1: {arg1}")
    print(f"args: {args}")
    print(f"kwarg1: {kwarg1}")
    print(f"kwargs: {kwargs}")

# Викликаємо функцію з позиційними та іменованими аргументами
mixed_function(1, 2, 3, 4, kwarg1="Hello", name="Alice", age=30)
# Виведе:
# arg1: 1
# args: (2, 3, 4)
# kwarg1: Hello
# kwargs: {'name': 'Alice', 'age': 30}



# function

# 1

def chunk_list(lst, size):
    return [lst[i:i + size] for i in range(0, len(lst), size)]

numbers = [1, 2, 3, 4, 5, 6, 7]
print(chunk_list(numbers, 3))  # Результат: [[1, 2, 3], [4, 5, 6], [7]]

# 2
def list_to_string(lst):
    return ", ".join(map(str, lst))

print(list_to_string([1, 2, 3, 4]))  # Результат: "1, 2, 3, 4"



# 3
def is_anagram(word1, word2):
    return sorted(word1.lower()) == sorted(word2.lower())

print(is_anagram("listen", "silent"))  # Результат: True
print(is_anagram("hello", "world"))    # Результат: False


# 4
def union_of_sets(*sets):
    return set().union(*sets)

set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = {5, 6, 7}

print(union_of_sets(set1, set2, set3))  # Результат: {1, 2, 3, 4, 5, 6, 7}

# 5
athletes = [("Alice", 15.2), ("Bob", 12.5), ("Charlie", 14.3)]

def sort_athletes(athletes):
    return sorted(athletes, key=lambda x: x[1])

print(sort_athletes(athletes))
# Результат: [('Bob', 12.5), ('Charlie', 14.3), ('Alice', 15.2)]

