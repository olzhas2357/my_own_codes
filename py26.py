# def draw_triangle(fill, base):
#     for i in range(base+1):
#         for j in range(i+1):
#             if  i + j < base:
#                 print(fill, end = "")
#         print()
# fill = input()
# base = int(input())
#
# draw_triangle(fill, base)
# #
# # объявление функции
# def print_fio(n, s, p):
#     print(s[0].upper() + n[0].upper() + p[0].upper())
# # считываем данные
# n, s, p = input(), input(), input()
#
# # вызываем функцию
# print_fio(n, s, p)

# объявление функции
def print_digit_sum(num):
    c = 0
    s = str(num)
    for i in range(len(s)):
        c+=int(s[i])
    print(c)
# считываем данные
n = int(input())

# вызываем функцию
print_digit_sum(n)