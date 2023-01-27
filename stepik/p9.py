
a = input()
l = a.find('h')
r = a.rfind('h')

for i in range(0, l+1):
    print(a[i], end="")
for i in range(l-1, r-1):
    print(a[-i], end="")
for i in range(r+1, len(a)):
    print(a[i], end= "")
