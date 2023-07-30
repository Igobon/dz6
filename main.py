# Завдання 1
#
# Напишіть функцію, яка обчислює добуток елементів списку цілих.
# Список передається як параметр. Отриманий результат повертається із функції.

import random
a=int(input("Enter the first number of list"))
b=int(input("Enter the last number of list"))
numbers=[random.randint(a,b) for number in range(1,10)]
print(numbers)

def dob_lst(numbers):
    dobutok=1
    for i in numbers:
        dobutok*=i

    print(f'dobutok all numbers of random list={dobutok}')


try:
    dob_lst(numbers)

except Exception as error:
    print(error)


# Завдання 2

# Напишіть функцію для знаходження мінімуму у списку цілих.
# Список передається як параметр. Отриманий результат повертається із функції.
import random
a=int(input("Enter the first number of list"))
b=int(input("Enter the last number of list"))
numbers=[random.randint(a,b) for number in range(1,10)]
print(numbers)

def min_n(numbers):
    min_n=min(numbers)

    print(f"minimal_number= {min_n}")

min_n(numbers)
# Завдання 3
#
# Напишіть функцію, яка визначає кількість простих чисел у списку цілих.
# Список передається як параметр. Отриманий результат повертається із функції.
import random


numbers = [random.randint(1, 10) for _ in range(10)]
print(numbers)

def simple_number(number):
    if number<2:
        return False
    for i in range(2,number):
        if number%i==0:
            return False
    return True

def count_simple(numbers):
    count = 0
    for number in numbers:
        if simple_number(number):
            count+=1
    return count
print(f"count of simple numbers{count_simple(numbers)}")

try:
    count_simple(numbers)
except Exception as error:
     print(error)

# Завдання 4
#
# Напишіть функцію, яка видаляє зі списку ціле задане число.
# З функції потрібно повернути кількість видаленних елементів.
import random
a=int(input("Enter the first number of list"))
b=int(input("Enter the last number of list"))
numbers=[random.randint(a,b) for number in range(1,10)]
print(numbers)


def del_nmb(numbers,number):
    count=0

    while number in numbers:
        numbers.remove(number)
        count+=1
    return count





number = int(input("Enter a delate number"))
count_of_number=del_nmb(numbers,number)
print(f"count of delate number{count_of_number}")

# Завдання 5
#
# Напишіть функцію, яка отримує два списки як параметр
# і повертає список, що містить елементи обох списків.
import random
a=int(input("Enter the first number of list"))
b=int(input("Enter the last number of list"))
numbers=[random.randint(a,b) for number in range(1,10)]
print(numbers)


def generate_list(list_len) -> list:
    numbers = []
    for i in range(list_len):
        numbers.append(random.randint(1, 100))

    return numbers

def doublelist(list1,list2):
    return list1+list2


list1=generate_list(5)
list2=generate_list(5)
print(doublelist(list1,list2))
print(list1)
print(list2)


# Завдання 6
#
# Напишіть функцію, яка обчислює ступінь кожного елемента списку цілих.
# Значення для ступеня передається як параметр, список також передається як параметр.
# Функція повертає новий список, який містить отримані результати.
import random
a=int(input("Enter the first number of list"))
b=int(input("Enter the last number of list"))
numbers=[random.randint(a,b) for number in range(1,10)]
print(numbers)
def step_of_number(numbers):

    degree=int(input("degree"))

    for i in range(len(numbers)):
        numbers[i]**=degree

    print(f"number after degree{numbers}")
try:
    step_of_number(numbers)
except Exception as error:
    print(error)

    print("finish")