# def function_name([parameters]):
#    [''' docstring''']
#    body | pass
#    [return expression]


def to_string(number):
    return str(number) + " now is string!"


def to_bool(value=False):
    return bool(value)

####################
def division(number1, number2):
    result = None
    if number2 != 0:
        result = number1 / number2
    return result


print(division(1, 0))
print(division(number2=0, number1=5))


################
def sum_of_int(*numbers):
    flag = True
    for n in numbers:
        if type(n) != int:
            flag = False
    if flag:
        return sum(*numbers)
    else:
        return None
############


def sum_of_int(*numbers):
    if is_int(*numbers):
        return sum(numbers)
    else:
        return None


def is_int(*numbers):
    for n in numbers:
        if type(n) != int:
            return False
    else:
        return True
###########


def sum_of_int(*numbers):
    return sum(numbers) if is_int(*numbers) else None


def is_int(*numbers):
    for n in numbers:
        if type(n) != int:
            return False
    else:
        return True
############


print(sum_of_int(3, 4, 1, 2, 0))
print(sum_of_int(3.1, 4, 1, 2, 0))
#################


def format_message(**kwargs):
    return ", ".join(f"{key}: {value}" for key, value in kwargs.items())


message = format_message(name="John", age=30, city="New York", occupation="Developer")
print(message)
######################

повторення закінчилось
#######################

# задача на всі аргументи
# задача на зміну данних в змінних типах і не зміну в незмінних
# задача на повернення кортежу

################ tasks
# передача аргументів
## 1
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# Приклади використання
print(greet("Alice"))  # Hello, Alice!
print(greet("Bob", "Hi"))  # Hi, Bob!


## 2
def sum_numbers(*args):
    return sum(args)

# Приклади використання
print(sum_numbers(1, 2, 3))  # 6
print(sum_numbers(5, 10, 15, 20))  # 50


## 3
def format_address(street, city, zipcode):
    return f"{street}, {city}, {zipcode}"

# Приклади використання
print(format_address(street="Main St.", city="Springfield", zipcode="12345"))
# "Main St., Springfield, 12345"


## 4
def rectangle_area(length, width=None):
    if width is None:
        width = length  # Квадрат
    return length * width

# Приклади використання
print(rectangle_area(5))  # 25
print(rectangle_area(5, 10))  # 50


## 5
def print_user_info(name, age, city="Unknown"):
    return f"{name}, {age} years old, lives in {city}."

# Приклади використання
print(print_user_info("Alice", 25))  # "Alice, 25 years old, lives in Unknown."
print(print_user_info("Bob", 30, city="New York"))  # "Bob, 30 years old, lives in New York."


## 6
def build_profile(first_name, last_name, **kwargs):
    profile = {"first_name": first_name, "last_name": last_name}
    profile.update(kwargs)
    return profile

# Приклади використання
print(build_profile("John", "Doe", age=30, location="New York", hobby="cycling"))
# {'first_name': 'John', 'last_name': 'Doe', 'age': 30, 'location': 'New York', 'hobby': 'cycling'}


#########################
# функції за замовчуванням
# 1
def print_message(msg, prefix="INFO"):
    print(f"[{prefix}] {msg}")

# Приклади використання
print_message("System started")  # [INFO] System started
print_message("User login failed", prefix="ERROR")  # [ERROR] User login failed


# 2
def sum_numbers(a, b=0):
    return a + b

# Приклади використання
print(sum_numbers(5))  # 5
print(sum_numbers(5, 10))  # 15


# 3
from datetime import datetime

def format_date(day, month=1, year=None):
    if year is None:
        year = datetime.now().year
    return f"{day:02d}-{month:02d}-{year}"

# Приклади використання
print(format_date(25))  # 25-01-2024 (поточний рік)
print(format_date(15, 7, 2023))  # 15-07-2023
print(format_date(1, 12))  # 01-12-2024




###############
# змінної кількості аргументів і іменованих аргументів
# 1
def concat_strings(*args):
    return ''.join(args)

# Приклади використання
print(concat_strings("Hello", " ", "World"))  # Hello World
print(concat_strings("Python", " is", " awesome"))  # Python is awesome


# 2
def max_number(*args):
    if args:
        return max(args)
    else:
        return None  # Якщо не передано аргументів

# Приклади використання
print(max_number(5, 10, 3, 8))  # 10
print(max_number(2, 7))  # 7
print(max_number())  # None


# 3
def print_user_info(**kwargs):
    info = ', '.join([f"{key}: {value}" for key, value in kwargs.items()])
    return info

# Приклади використання
print(print_user_info(name="Alice", age=25, country="USA"))
# name: Alice, age: 25, country: USA

print(print_user_info(name="Bob", job="Engineer"))
# name: Bob, job: Engineer


# 4
def student_score(name, subject, *scores):
    if scores:
        average = sum(scores) / len(scores)
        return f"Student: {name}, Subject: {subject}, Average score: {average:.2f}"
    else:
        return "No scores provided."

# Приклади використання
print(student_score("Alice", "Math", 90, 85, 88))
# Student: Alice, Subject: Math, Average score: 87.67

print(student_score("Bob", "Physics"))
# No scores provided.


# 5
def total_sum(*args, multiplier=1):
    return sum(args) * multiplier

# Приклади використання
print(total_sum(1, 2, 3, 4, multiplier=2))  # 20
print(total_sum(5, 10, 15))  # 30 (без множника)



##############
# Розпакування кортежу чи словника в низку фактичних параметрів
# 2
def create_account(username, email, password):
    return f"Account created for {username} with email {email}."

# Словник з параметрами для функції
account_info = {
    "username": "john_doe",
    "email": "john@example.com",
    "password": "securepassword123"
}

# Розпакування словника та передача значень
print(create_account(**account_info))  # Account created for john_doe with email john@example.com.


# 3
def multiply_numbers(*args):
    result = 1
    for number in args:
        result *= number
    return result

# Кортеж з числами
numbers = (2, 3, 4)

# Розпакування кортежу та передача значень
print(multiply_numbers(*numbers))  # 24


# 4
def set_device_settings(brightness, contrast, volume):
    return f"Settings - Brightness: {brightness}, Contrast: {contrast}, Volume: {volume}"

# Словник з налаштуваннями
device_settings = {
    "brightness": 75,
    "contrast": 50,
    "volume": 30
}

# Розпакування словника та передача значень
print(set_device_settings(**device_settings))  # Settings - Brightness: 75, Contrast: 50, Volume: 30


# 5
def process_data(name, age, profession):
    return f"Name: {name}, Age: {age}, Profession: {profession}"

# Кортеж з даними
user_data = ("Alice", 30, "Engineer")

# Розпакування кортежу та передача значень
print(process_data(*user_data))  # Name: Alice, Age: 30, Profession: Engineer


# 6
def build_profile(first_name, last_name, email, age):
    return f"Profile: {first_name} {last_name}, Email: {email}, Age: {age}"

# Словник з даними користувача
profile_data = {
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com",
    "age": 28
}

# Розпакування словника та передача значень
print(build_profile(**profile_data))  # Profile: John Doe, Email: john.doe@example.com, Age: 28



####################################
# Функція очікує позиційні аргументи, іменовані аргументи, або можливість використовувати обидва типи
# 1
def create_user(username, email, age=18, country="Unknown"):
    return {
        "username": username,
        "email": email,
        "age": age,
        "country": country
    }

# Приклади використання
print(create_user("Alice", "alice@example.com"))
# {'username': 'Alice', 'email': 'alice@example.com', 'age': 18, 'country': 'Unknown'}

print(create_user("Bob", "bob@example.com", age=25, country="USA"))
# {'username': 'Bob', 'email': 'bob@example.com', 'age': 25, 'country': 'USA'}


# 2
def book_info(title, author, year, genre="Unknown", pages=0):
    return f"Title: {title}, Author: {author}, Year: {year}, Genre: {genre}, Pages: {pages}"

# Приклади використання
print(book_info("The Great Gatsby", "F. Scott Fitzgerald", 1925))
# Title: The Great Gatsby, Author: F. Scott Fitzgerald, Year: 1925, Genre: Unknown, Pages: 0

print(book_info("1984", "George Orwell", 1949, genre="Dystopian", pages=328))
# Title: 1984, Author: George Orwell, Year: 1949, Genre: Dystopian, Pages: 328


# 3
def register_event(event_name, event_date, location="Online", capacity=100):
    return {
        "event_name": event_name,
        "event_date": event_date,
        "location": location,
        "capacity": capacity
    }

# Приклади використання
print(register_event("Python Workshop", "2024-12-20"))
# {'event_name': 'Python Workshop', 'event_date': '2024-12-20', 'location': 'Online', 'capacity': 100}

print(register_event("Tech Conference", "2024-12-22", location="New York", capacity=500))
# {'event_name': 'Tech Conference', 'event_date': '2024-12-22', 'location': 'New York', 'capacity': 500}


# 4
def make_order(*items, total_price=0):
    return {
        "items": items,
        "total_price": total_price
    }

# Приклади використання
print(make_order("Laptop", "Phone", total_price=1500))
# {'items': ('Laptop', 'Phone'), 'total_price': 1500}

print(make_order("Book", "Pen", "Notebook", total_price=30))
# {'items': ('Book', 'Pen', 'Notebook'), 'total_price': 30}


# 5
def create_profile(name, email, phone, address="Not provided"):
    return f"Name: {name}, Email: {email}, Phone: {phone}, Address: {address}"

# Приклади використання
print(create_profile("Alice", "alice@example.com", "123-456-7890"))
# Name: Alice, Email: alice@example.com, Phone: 123-456-7890, Address: Not provided

print(create_profile("Bob", "bob@example.com", "987-654-3210", address="123 Main St"))
# Name: Bob, Email: bob@example.com, Phone: 987-654-3210, Address: 123 Main St




#################
# Робота з глобальними і локальними змінними

# 1
# Глобальна змінна
counter = 0

def increment_counter():
    global counter
    counter += 1

def reset_counter():
    global counter
    counter = 0

# Приклад використання
increment_counter()
increment_counter()
print(counter)  # 2
reset_counter()
print(counter)  # 0


# 2
# Глобальна змінна
message = ""

def create_message(new_message):
    global message
    message += new_message + " "

def clear_message():
    global message
    message = ""

# Приклад використання
create_message("Hello")
create_message("world!")
print(message)  # "Hello world! "
clear_message()
print(message)  # ""


# 3
# Глобальна змінна (кортеж)
allowed_users = ("admin", "manager")

def check_access(user):
    return user in allowed_users

def add_user(new_user):
    global allowed_users
    allowed_users = allowed_users + (new_user,)

# Приклад використання
print(check_access("admin"))  # True
add_user("guest")
print(check_access("guest"))  # True


# 4
# Глобальна змінна
order_status = "Pending"

def update_order_status(new_status):
    global order_status
    order_status = new_status

def reset_order_status():
    global order_status
    order_status = "Pending"

# Приклад використання
print(order_status)  # "Pending"
update_order_status("Shipped")
print(order_status)  # "Shipped"
reset_order_status()
print(order_status)  # "Pending"


# 5
# Глобальна змінна (кортеж)
user_logins = ("user1", "user2")

def track_user_login(user):
    global user_logins
    user_logins += (user,)

def add_login_entry(user):
    track_user_login(user)

# Приклад використання
print(user_logins)  # ('user1', 'user2')
add_login_entry("user3")
print(user_logins)  # ('user1', 'user2', 'user3')


# 6
# Глобальна змінна
total = 0

def add_to_total(value):
    global total
    total += value

def reset_total():
    global total
    total = 0

# Приклад використання
add_to_total(10)
add_to_total(20)
print(total)  # 30
reset_total()
print(total)  # 0






