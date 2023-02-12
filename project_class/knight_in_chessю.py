
N = input()
a1 = ord(N[0]) - 96
a2 = int(N[1])
l = [8, 7, 6, 5, 4, 3, 2, 1]
for i in l:
    for j in range(1, 9):
        if i == a2 and  j == a1:
            print("N", end = " ")
        elif (a2 - i)**2 + (a1-j)**2 == 5:
            print("*", end = " ")
        else:
            print(".", end = " ")
    print()
