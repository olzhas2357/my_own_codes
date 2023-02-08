def space(n):
    sum = 0
    m = ""
    for i in range(len(n)):
        if n[i] == " " and n[i + 1] == " ":
            m += ""
        else:
            m += n[i]
    for i in range(len(m)):
        if m[i] == " ":
            sum += 1
    return sum + 1
n= input()
print(space(n))


print(len(input().split()))

def horoscope(n):
    animals = ['Обезьяна', 'Петух', 'Собака', 'Свинья', 'Крыса', 'Бык', 'Тигр', 'Заяц', 'Дракон', 'Змея', 'Лошадь', 'Овца']
    for i in range(0, len(animals)):
        if n % 12 == i:
            print(animals[i])

n = int(input())
horoscope(n)


def reverse(c):
    l = []
    for i in range(len(c)):
        if c[i] == "0":
            continue
    print(int(c))
n = input()
c = ""
m = len(n)
if m == 6:
    c = n[0] + n[:0:-1]
else:
    c = n[::-1]
reverse(c)

def point(num):
    for i in range(len(num) - 3, 0, -3):
#     num = num[:i]+","+num[i:]

n = input()
point(n)


num = input()
for i in range(len(num) - 3, 0, -3):
    num = num[:i]+","+num[i:]
print(num)

num = int(input())
print(f'{num:,}')