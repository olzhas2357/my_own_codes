
# n = int(input())
# sum_1, sum_2, sum_3, sum_4 = 0, 0, 0, 0
# for i in range(n):
#     k = input()
#     l = k.split()
#
#     if int(l[0]) > 0 and int(l[1]) > 0:
#         sum_1 += 1
#     elif int(l[0]) < 0 and int(l[1]) > 0:
#         sum_2 += 1
#     elif int(l[0]) < 0 and int(l[1]) < 0:
#         sum_3 += 1
#     elif int(l[0]) > 0 and int(l[1]) < 0:
#             sum_4 +=1
# print(f"Первая четверть: {sum_1}")
# print(f"Вторая четверть: {sum_2}")
# print(f"Третья четверть: {sum_3}")
# print(f"Четвертая четверть: {sum_4}")

# def shift(lst, steps):
#     if steps < 0:
#         steps = abs(steps)
#         for i in range(steps):
#             lst.append(lst.pop(0))
#     else:
#         for i in range(steps):
#             lst.insert(0, lst.pop())
# n = input()
# k = n.split()
# shift(k, 1)
# print(" ".join(k))
#




