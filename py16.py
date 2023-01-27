n = int(input())
l = []
b = 0
sum = 0
for i in range(n):
    a = int(input())
    sum = b + a
    b = a
    l.append(sum)
    sum = 0
del l[0]
print(l)