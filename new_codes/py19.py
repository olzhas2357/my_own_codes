
n = int(input())
l = []
for i in range(n):
    c = int(input())
    l.append(c)
max1 = max(l)
min1 = min(l)
l.remove(max1)
l.remove(min1)
for num in l:
    print(num)