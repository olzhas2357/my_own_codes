a = int(input())
l1 = []
l2 = []
l3 = []
l = []
for i in range(a):
    n = int(input())
    if n < 0:
        l1.append(n)
    elif n == 0:
        l2.append(n)
    elif n > 0:
        l3.append(n)
l.extend(l1)
l.extend(l2)
l.extend(l3)
print(l)