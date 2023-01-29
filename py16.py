
n = int(input())
l = []
for i in range(n):
    c = input()
    l.append(c)
s = input()
for i in range(len(l)):
    if s.lower() in l[i].lower():
        print(l[i])