# set - {}
# list - []

# methods a.pop() a.remove(5) a.discard()

a = int(input())
l = []
for i in range(a):
    c = int(input())
    l.append(c)

l.remove(3)
l.pop()
print(l)