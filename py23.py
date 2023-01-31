
n = input()
w = n.split()
max1 = -9999999
ind1, ind2 = 0, 0
min1 = 10000000
for i in range(len(w)):
    if max1 < int(w[i]):
        max1 = int(w[i])
        ind1 = i
for i in range(len(w)):
    if min1 > int(w[i]):
        min1 = int(w[i])
        ind2 = i

w[ind1] = min1
w[ind2] = max1
for num in w:
    print(num, end=" ")


# or

n = input()
l = n.split()
x = l.index(min(l))
y = l.index(max(l))
l[x], l[y] = max(l), min(l)
print(*l)