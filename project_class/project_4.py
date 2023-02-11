# # камень
# # бумага
# # ножницы
# #1Тимур
# #2Руслан
n = input()
m = input()
if n == m:
    print("ничья")
elif (n == "камень" and m == "бумага") or (n == "ножницы" and m == "камень") or (n == "бумага" and m == "ножницы"):
    print("Руслан")
else:
    print("Тимур")

s = [int(input()) for _ in range(int(input()))]
s1 = int(input())
flag = 'НЕТ'
for i in range(len(s)):
    for j in range(i + 1, len(s)):
        if s[i] * s[j] == s1:
            flag = 'ДА'
print(flag)

"anton"

def find_anton(c):
    m = "anton"
    l = ""
    anton = ""
    for i in range(len(m)):
        for j in range(len(c)):
            if m[i] == c[j]:
                l += c[j]
    for j in range(len(l)):
        if l[j] not in anton:
            anton += l[j]
    return anton + "n"
n = int(input())
for i in range(n):
    c = input()
    ind = i
    # if find_anton(c) == True:
    if find_anton(c) == "anton":
        print(ind+1, end = " ")

word = input() + " запретил букву"
alph = [chr(i) for i in range(1072, 1104) if chr(i) != "ё"]
for i in alph:
    if i in word:
        print(word, i)
        word = word.replace(i, "").replace("  ", " ").strip()


n, m = int(input()), int(input())    # считываем значения n и m
my_list = []

for _ in range(n):
    my_list.append([0] * m)

print(my_list)
l = []
n = int(input())
for i in range(n):
    l.append([j+1 for j in range(0, i+1)])
print(*l,sep = "\n")
def fact_formula(n, k):
    return int(fact(n)/(fact(n - k) * fact(k)))


def fact(n):
    if n == 0 or n == 1:
        return 1
    return fact(n-1)*n

l = []
n = int(input())
for i in range(0, n+1):
    l.append([fact_formula(i, j) for j in range(i + 1)])
print(l[n])


s = input().split()
lst = [[s[0]]]
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        lst[-1].append(s[i])
    else:
        lst.append([s[i]])

print(lst)

from itertools import groupby

st = input()
result = []
for i, j in groupby(st.split()):
    result.append(list(j))

print(result)

