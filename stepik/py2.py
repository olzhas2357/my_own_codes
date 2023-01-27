a = input()
s = ""
for i in range(len(a)):
    if a[i] == " ":
        s += a.replace(" ", "")
if s.isalpha() == True:
    print("Цифр нет")
else:
    print("Цифра")