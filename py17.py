

w = input().split()
for i in range(len(w)):
    w[i] = int(w[i])
w.sort()
for num in w:
    print(num, end=" ")
print()
w.sort(reverse = True)
for sum in w:
    print(sum, end =" ")

# or

w = input().split()
for i in range(len(w)):
    w[i] = int(w[i])
w.sort()
print(*w)
w.sort(reverse = True)
print(*w)