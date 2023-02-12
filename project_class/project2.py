# def find_anton(c):
#     m = "anton"
#     l = ""
#     anton = ""
#     for i in range(len(m)):
#         for j in range(len(c)):
#             if m[i] == c[j]:
#                 l += c[j]
#     for j in range(len(l)):
#         if l[j] not in anton:
#             anton += l[j]
#     return anton + "n"
# n = int(input())
# for i in range(n):
#     c = input()
#     ind = i
#     # if find_anton(c) == True:
#     if find_anton(c) == "anton":
#         print(ind+1, end = " ")


virus = 'anton'
for i in range(1, int(input())+1):
    s = input()
    res = ''
    for x in virus:
        if x in s:
            res += x
            s = s[s.find(x):]
        if res == virus:
            print(i, end = " ")

