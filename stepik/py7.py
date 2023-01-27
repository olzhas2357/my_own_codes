n = input()
sum = 0
if n.isalpha() == True:
    print(0)
else:
    for i in range(len(n)):
        if n[i] in "0123456789":
            sum += 1
print(sum)