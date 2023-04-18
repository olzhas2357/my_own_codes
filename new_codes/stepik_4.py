# students = [tuple(input().split()) for _ in range(int(input()))]
#
# for student in students:
#     print(*student)
#
# print()
#
# for name, grade in students:
#     if int(grade) > 3:
#         print(name, grade)
#
#
# class FirstNumbers:
#     def __init__(self, n):
#         self.last_number = n
#         self.current_number = 0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.current_number < self.last_number:
#             self.current_number += 1
#             return self.current_number - 1
#         raise StopIteration
#
#
# for i in FirstNumbers(n = 5):
#     print(i)
#
#
# 1
# x = 300
# def myfunc():
#     x = 200
#     print(x)
#
# myfunc()
# print(x)
#
# 200
# 300
#
# when we use global then
# x = 300
#
# def myfunc():
#     global x
#     x = 200
#
# myfunc()
#
# print(x)
#
#
#
# import datetime
#
# x = datetime.datetime.now()
# print(x.year)
# print(x.strftime("%a"))
# print(x.strftime("%w"))
# print(x.strftime("%d"))
# print(x.strftime("%b"))
# print(x.strftime("%m"))
# print(x.strftime("%H"))
# def count(n):
#     print("Hello from count")
#     idx = 0
#     while idx < n:
#         yield idx
#         idx += 1
#
#
# def display():
#     print("Hello world")
#
# counter_obj = count(n = 5)
#
# display()


# def producer():
#     for item in range(1, 6):
#         yield item
#
# def processing_1(sequence_gen):
#     for item in sequence_gen:
#         yield item * 2
#
# def consumer(sequence_gen):
#     for item in sequence_gen:
#         print(f"result item - {item}")
#
#
# producer1 = producer()
# proc1 = processing_1(sequence_gen = producer1)
# consumer(sequence_gen = proc1)


#
# class Factory:
#
#     def __init__(self, employees: list):
#         self.employees = employees
#
#     def __getitem__(self, idx):
#         return self.employees[idx]
#
#     def __len__(self):
#         return len(self.employees)
#
# class Human:
#
#     def __init__(self, name, city):
#         self.name = name
#         self.city = city
#
#     def __str__(self):
#         return f"Human(name={self.name})"
#
# empl = [Human(name='aibek', city='almaty'), Human(name='aida', city = 'astana')]
#
# factory = Factory(employees=empl)
#
# print(
#     factory[1],
#     len(factory),
# )

# def chain(list1, list2):
#     yield from list1
#     yield from list2
#
# a = [1, 2, 3]
# b = [4, 5, 6]
#
# for i in chain(a, b):
#     print(i, end = " ")


#
# my_dict = {1.12: 'aa', 67.9: 45, 3.11: 'ccc', 7.9: 'dd', 9.2: 'ee', 7.1: 'ff', 0.12: 'qq', 1.91: 'aa', 10.12: [1, 2, 3], 99.0: {9, 0, 1}}
#
# max_value = max(my_dict)
# min_value = min(my_dict)
# print(max_value + min_value)
# users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
#          {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
#          {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
#          {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
#          {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
#          {'name': 'John', 'phone': '233-421-32', 'email': ''},
#          {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
#          {'name': 'Alina', 'phone': '+7948-799-2434', 'email': 'ali.ch.b@gmail.com'},
#          {'name': 'Robert', 'phone': '420-2011', 'email': ''},
#          {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
#          {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
#          {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
#          {'name': 'Roman', 'phone': '+7459-145-8059', 'email': 'roma988@mail.ru'},
#          {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
#          {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
#          {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
# l = []
# for i in range(len(users)):
#     if users[i]['phone'][-1] == '8':
#         l.append(users[i]['name'])
# s = sorted(l)
# print("\n".join(s))


# def my_generator(n):
#
#     value = 0
#
#     while value < n:
#         yield value
#         value += 1
#
# for i in my_generator(8):
#     print(i)


import json

# def producer(n):
#     i = 0
#     while i < n:
#         yield i
#         i += 1
#
# def processing(sequence):
#     for item in sequence:
#         yield item + 5
#
# def consumer(sequence):
#     for item in sequence:
#         yield f"prepared item {item}"
#
# a = producer(n=5)
# b = processing(sequence=a)
# c = consumer(sequence=b)
# for element in c:
#     print(element)

# class Human:
#     def __init__(self):
#         self.name = 'roma'
#
# class HumanEncodes(json.JSONEncoder):
#     def default(self, o):
#         return o.__dict__
#
# obj = json.dumps(Human(), cls=HumanEncodes)
# print(obj, type(obj))


from decimal import*
# num = Decimal('10.0')
# print(num.sqrt())
# print(num.ln())
# print(num.exp())
# print(num.log10())
# num1 = Decimal(1.4568123546)
# num2 = Decimal(0.1654551651)
# print(num1.as_tuple())
# print(num2.as_tuple())

from decimal import *

# num = Decimal('-1.4568769017')
# num_tuple = num.as_tuple()
#
# print(num_tuple.sign)
# print(num_tuple.digits)
# print(num_tuple.exponent)

s = '0.77 4.03 9.06 3.80 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 1.46 5.26 4.83 7.23 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 0.03 9.60 8.86 2.73 5.83 6.50'
num1 = max(s)
num2 = min(s)
print(num1 + num2)
