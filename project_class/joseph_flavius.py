n, k = int(input()), int(input())
s = []
for i in range(n):
    s.append(i+1)
while len(s) > 1:
    for i in range(0, k-1):
        s.append(s[i])
    del s[:k]
print(*s)