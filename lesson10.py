import sys

v_lst = [i * 2 for i in range(10000)]
g_lst = (i * 2 for i in range(10000)) # генератор, не список

print(sys.getsizeof(v_lst))
print(sys.getsizeof(g_lst)) # байти
# print(list(g_lst))
# print(list(g_lst))

g_lst = (i * 2 for i in range(1_000_000_000_000))
print(sys.getsizeof(g_lst)) # байти


g_lst = (i * 2 for i in range(10))
print(list(g_lst))
print(g_lst)
print(list(g_lst))
print(bool(g_lst))


g_lst = (i * 2 for i in range(1000))

for i in g_lst:
    print(i, end=" ")
    if i == 36:
        break

print(" ")

for i in g_lst:
    print(i, end=" ")
    if i == 100:
        break

print(" ")

print(next(g_lst))


#####################

a = [4, 8, 0, 6, 2, 10]
b = [x for x in a if x % 2]
c = (x for x in a if x % 2)

print(b)

if b:
    print("List exist")

if c:
    print("Gen exist")
    print(list(c))


#######

squares = (x ** 2 for x in range(10))
print(next(squares))  # Виведе 0
print(next(squares))  # Виведе 1
print(next(squares))  # Виведе 4


############ замикання

def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function


closure = outer_function(10)
print(closure.__closure__)  # Виведе інформацію про замикання
# Переглянемо значення збереженої змінної
print(closure.__closure__[0].cell_contents)  # Виведе 10



############  Параметризований декоратор для логування рівня важливості повідомлень


def log(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"[{level}] Викликається функція {func.__name__} з аргументами: {args}, {kwargs}")
            return func(*args, **kwargs)
        return wrapper
    return decorator


@log("INFO")
def add(a, b):
    return a + b


@log("ERROR")
def divide(a, b):
    if b == 0:
        raise ValueError("Не можна ділити на 0")
    return a / b


print(add(3, 5))  # INFO
print(divide(10, 0))  # ERROR

#####################


# Приклад: Декоратор для логування часу виконання функції
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Записуємо час до виконання функції
        result = func(*args, **kwargs)  # Викликаємо функцію
        end_time = time.time()  # Записуємо час після виконання функції
        print(f"{func.__name__} виконувалась {end_time - start_time:.4f} секунд")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)

slow_function()  # Виведе час виконання функції


# Декоратор для перевірки правильності аргументів
def validate_positive(func):
    def wrapper(*args, **kwargs):
        if any(arg <= 0 for arg in args):  # Перевіряємо, чи є невід'ємні аргументи
            raise ValueError("Аргументи повинні бути додатними!")
        return func(*args, **kwargs)
    return wrapper

@validate_positive
def add(a, b):
    return a + b

print(add(1, 2))  # 3
print(add(-1, 2))  # ValueError: Аргументи повинні бути додатними!



# Приклад: Декоратор для кешування результатів:
def memoize(func):
    cache = {}  # Словник для кешування
    def wrapper(*args):
        if args in cache:  # Перевіряємо, чи є результат в кеші
            return cache[args]
        result = func(*args)
        cache[args] = result  # Кешуємо результат
        return result
    return wrapper

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))  # Швидше, оскільки повторні виклики кешуються

####
# область видимості параметра н належить до зовнішньої функції, проте вкладена функція
# може вмкористовувати його

def calculate_pow(n):
    def calculate(number):
        print(locals())
        return number ** n
    return calculate


f = calculate_pow(3)
print(f)
# <function calculate_pow.,locals>.calculate at 0xgagdfgs>

number_one = f(2)
print(number_one)

number_two = f(5)
print(number_two)

func = calculate_pow(5)
print(func(3))
# {"number" : 3, "n" : 5}

###############################
# коли ми застосовуємо декоратор для якоїсь функції, інтерпретатор за умовчанням передає цю
# функцію як аргумент декоратора

my_function = []


def add_function(func):
    my_function.append(func)
    return func


@add_function
def summ(x, y):
    return x + y

@add_function
def mul(x, y):
    return x * y


print(my_function)
print(mul(4, 5))


def div(x, y):
    return x / y


div = add_function(div)


print(my_function)


#############
 Приклад: Сендвіч з правильним порядком виведення

# Декоратор для хліба
def bread(func):
    def wrapper(*args, **kwargs):
        print("Хліб")
        result = func(*args, **kwargs)
        return result
    return wrapper

# Декоратор для салату
def salad(func):
    def wrapper(*args, **kwargs):
        print("Салат")
        result = func(*args, **kwargs)
        return result
    return wrapper

# Декоратор для ковбаси
def sausage(func):
    def wrapper(*args, **kwargs):
        print("Ковбаса")
        result = func(*args, **kwargs)
        return result
    return wrapper

# Декоратор для сиру
def cheese(func):
    def wrapper(*args, **kwargs):
        print("Сир")
        result = func(*args, **kwargs)
        return result
    return wrapper

# Основна функція, до якої застосовуються декоратори
@cheese
@sausage
@salad
@bread
def make_sandwich():
    print("Готово! Сендвіч зроблено.")

# Викликаємо функцію з декількома декораторами
make_sandwich()
