
n = int(input())
l1, l2 = list(), list()
for _ in range(n):
    l1.append(input())
k = int(input())
for _ in range(k):
    l2.append(input())
sum = 0
for q in range(n):
    for j in range(k):
        if l2[j].lower() in l1[q].lower():
            sum += 1
    if sum == k:
        print(l1[q])
    sum = 0
