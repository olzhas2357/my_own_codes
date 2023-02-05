
a = int(input())
l1, l2, l3, l = list(), list(), list(), list()
for i in range(a):
    n = int(input())
    if n < 0:
        l1.append(n)
    elif n == 0:
        l2.append(n)
    elif n > 0:
        l3.append(n)
print(*l1, *l2, *l3, sep="\n")


n = int(input())
l = []
for i in range(n):
    c = input()
    l.append(c)

new = []
s = input()

for let in l:
    for i in range(len(let)):
        if s in let:
            k = let
            if let not in new:
                new.append(let)
for pro in new:
    print(pro)