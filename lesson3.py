# Decimal
print(1.1 + 2.2 == 3.3)
print(int(1.1) + int(2.2) == int(3.3))

import decimal

print(0.1 + 0.1 + 0.1 - 0.3)

print((decimal.Decimal('0.1') + decimal.Decimal('0.1') + decimal.Decimal('0.1') - decimal.Decimal('0.3')))
print((decimal.Decimal(0.1) + decimal.Decimal(0.1) + decimal.Decimal(0.1) - decimal.Decimal(0.3)))

decimal.getcontext().prec = 4
print(decimal.Decimal(1) / decimal.Decimal(7))  #Decimal('0.1429')
print(decimal.Decimal(0.1) + decimal.Decimal(0.1) + decimal.Decimal(0.1) - decimal.Decimal(0.3)) # Decimal('1.110E-17')


# fractions
import fractions
x = fractions.Fraction(1, 3)
y = fractions.Fraction(4, 6)
print(y) # 2/3
print(x + y) # 1
print(x - y) # -1/3
print(x * y) # 2/9


############################
print(2.0 == 2.0)
print(2.0 != 2.0)
print(2.0 > 1)
print(1 < 2)
print(2.0 >= 2)
print(11 <= 2)


x = 2
y = 4
z = 8

print(1 + "1")
print("he" in "hello")
print("He" in "hello")
print("he" not in "hello")

print(15 == 15.00)
# print(15 is 15.00)

a = None
print(a is None)
# Використовуйте is лише тоді, коли вам потрібно
# перевірити, чи є два об'єкти одним і тим самим
# екземпляром (наприклад, для перевірки None)


# if
# 1
number = int(input("Введіть число: "))
if number % 2 == 0:
    print("Парне")
else:
    print("Непарне")
# 2
a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))
c = int(input("Введіть третє число: "))

if a >= b and a >= c:
    print("Максимальне число:", a)
elif b >= a and b >= c:
    print("Максимальне число:", b)
else:
    print("Максимальне число:", c)
# 3
age = int(input("Введіть свій вік: "))

if age >= 0 and age <= 12:
    print("Дитина")
elif age >= 13 and age <= 18:
    print("Підліток")
elif age >= 19 and age <= 60:
    print("Дорослий")
else:
    print("Пенсіонер")


operators
# 1
age = int(input("Введіть ваш вік: "))
print("Ви можете голосувати:", age >= 18)
# 2
a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))
print(f"{a} є квадратом {b}:", a == b ** 2)
# 3
num = int(input("Введіть число: "))
print("Число парне:", num % 2 == 0)


print(x < y < z)
print((x < y) and (y < z))

print(x < y > z)
print(x < y and y > z)

print(1 < 2 < 3.0 < 4)
print(1 > 2 > 3.0 > 4)

print(1 == 2 < 3)
print(1 ==2 and 2 < 3)


# bool
# 1
num = int(input("Введіть число: "))
print("Число парне і більше 10:", num % 2 == 0 and num > 10)
# 2
num = int(input("Введіть число: "))
print("Число входить у діапазон від 1 до 20 або є парним:", 1 <= num <= 20 or num % 2 == 0)
# 3
num = int(input("Введіть число: "))
print("Число не входить у діапазон:", not (10 <= num <= 50))


# Як створити порожній список у Python
lst = []
list3 = list()

len(lst)

print(dir(list))

my_list = [10, 20, 30, 40, 50, 60]
sub_list = my_list[1:4]
print(sub_list)  # [20, 30, 40]


# list
# 1
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[::2])  # [1, 3, 5, 7, 9]
# 2
numbers = [1, 2, 3, 4, 5]
print(numbers[:-1])  # [1, 2, 3, 4]
# 3
numbers = [1, 2, 3, 4, 5]
print(numbers[-3:])  # [3, 4, 5]


#######
# Отримуємо вік та статус студента від користувача
age_input = input("Введіть ваш вік: ")

# Перевірка, чи ввів користувач ціле число для віку
if age_input.isdigit():
    age = int(age_input)
    is_student_input = input("Ви студент? (так/ні): ").lower()

    # Перетворюємо відповідь на булеве значення
    if is_student_input == "так":
        is_student = True
    elif is_student_input == "ні":
        is_student = False
    else:
        print("Помилка: введено невірну відповідь щодо студентства!")
        is_student = None  # Призначаємо значення None, щоб не виконувати подальші перевірки

    if is_student is not None:
        # Перевіряємо, чи може користувач взяти участь в заході
        if age >= 18:
            # Вкладений if: перевірка на студентський статус
            if is_student:
                print("Ви можете взяти участь в заході зі знижкою!")
            else:
                print("Ви можете взяти участь в заході без знижки.")
        else:
            print("Ви не можете взяти участь в заході, бо вам менше 18 років.")
else:
    print("Помилка: введено неправильний вік!")
