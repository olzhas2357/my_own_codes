a = input()
w = a.split()
s = []
for let in w:
    s.append(let[0])
d = '.'.join(s)
print(d+".")


n = input()
l = n.split(chr(92))
for num in l:
    print(num)

n = input()
k = 0
for i in range(len(n)):
    if n[i] != 0:
        k = int(n[i])
        print("+" * k)

n = input().split()
for num in n:
    if num.isdigit():
        print(int(num) * "+")

n = input()
sum = 0
numbers = n.split(".")
for num in numbers:
    if 0 <= int(num) < 255:
        sum += 1
if sum == 4:
    print("ДА")
else:
    print("НЕТ")



n = input()
s = input()
for i in range(len(n)):
    if i+1 != len(n):
        print(n[i], end = f"{s}")
    else:
        print(n[i], end = "")

