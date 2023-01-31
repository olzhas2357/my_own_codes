a = [17, 24, 91, 96, 67, -27, 79, -71, -71, 58, 48, 88, 88, -16, -78, 96, -76, 56, 92, 1, 32, -17, 36, 88, -61, -97, -37, -84, 50, 47, 94, -6, 52, -76, 93, 14, -32, 98, -65, -16, -9, -68, -20, -40, -71, 93, -91, 44, 25, 79, 97, 0, -94, 7, -47, -96, -55, -58, -78, -78, -79, 75, 44, -56, -41, 38, 16, 70, 17, -17, -24, -83, -74, -73, 11, -26, 63, -75, -19, -13, -51, -74, 21, -8, 21, -68, -66, -84, -95, 78, 69, -29, 39, 38, -55, 7, -11, -26, -62, -84]

n = len(a)

for i in range(n - 1):
    for j in range(n - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print(a)

def draw_box():
    for _ in range(5):
        print('*' * 7)
draw_box()
print()
draw_box()
print()
draw_box()

def print_message():
    print('Я - Артур,')
    print('король британцев. ')

# вызов функции
print_message()


def draw_triangle():
    n = 11
    for i in range(n):
        for j in range(i):
            print("*", end= "")
        print()

draw_triangle()

for i in range(14):
    if i == 0 or i == 13:
        print("*" * 10)
    else:
        print('*'+' ' *8 + '*')


def draw_box():
    for i in range(14):
        if i == 0 or i == 13:
            print("*" * 10)
        else:
            print("*" + " " * 8 + "*")
draw_box()

def draw_box(height, width):    # функция принимает два параметра
    for i in range(height):
        print('*' * width)
draw_box(15, 7)