a = int(input())
l = []
if a <= 26:
    for i in range(a):
        c = chr(97 + i) * (i+1)
        l.append(c)
print(l)