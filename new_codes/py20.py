# put your python code here
# unique
n = int(input())
l = []
for i in range(n):
    s = input()
    l.append(s)
unique = list(set(l))
for num in unique:
    print(num)
# new method
n = int(input())
l = []
for i in range(n):
    s = input()
    if s not in l:
        l.append(s)
for num in l:
    print(num)


