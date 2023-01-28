a = input()

for i in range(len(a)):
    s = a[i]*(i+1)
    if ((i + 1) != len(a)):
        print(s.capitalize(), end = "-")
    else:
        print(s.capitalize(), end="")