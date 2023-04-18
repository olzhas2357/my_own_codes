# import math
# def my_function(num):
#     flag = 0
#
#     if num == 1:
#         flag = 0
#     elif num > 1:
#         # check for factors
#         for i in range(2, num):
#             if (num % i) == 0:
#                 # if factor is found, set flag to True
#                 flag = 0
#                 # break out of loop
#                 break
#             else:
#                 flag = 1
#     return flag
# l = [int(input()) for i in range(int(input()))]
# p = map(my_function, l)
# print(list(p))
# print(l)

# def producer():
#     for item in range(0, 3):
#         yield item
# def processing(sequence):
#     for item in sequence:
#         print(f'processing {item}')
#         yield item * 2
# def consumer(sequence):
#     for item in sequence:
#         yield f'prepared item {item}'
#
# pr = producer()
# process1 = processing(sequence = pr)
# result = consumer(process1)
# for elem in result:
#     print(elem)
# class RangeAnalog:
#     def __init__(self, n):
#         self.end_number = n # 4
#         self.current_number = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current_number < self.end_number:
#             self.current_number += 1
#             return self.current_number - 1
#         raise StopIteration()
#
#
# # simple_range = RangeAnalog(n=5)
# for i in RangeAnalog(n=4):
#     print(i)
