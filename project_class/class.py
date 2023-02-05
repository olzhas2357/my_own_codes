class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.045, -4.45)
y = Complex(4.12, -78)
print(y.r, y.i)
print(x.r, x.i)

class Dog:
    kind = 'barbos'

    def __init__(self, name):
        self.name = name

d = Dog('figo')
print(d.name)
D = Dog.kind
print(D)
e = Dog('buddy')
print(e.name)

class Dog:

    def __init__(self, name):
        self.name = name
        self.l = []
    def add_trick(self, trick):
        self.l.append(trick)
d = Dog('Figo')
y = Dog('Barbod')
d.add_trick('roll over')
y.add_trick('play dead')
print(d.l)
print(y.l)

class Upper:

    def __init__(self, name):
        self.name = name

    def print_String(self):
        print("Purchase course : ", self.name.upper())


Upper.print_String = classmethod(Upper.print_String)
Upper.print_String()
#
class Light:
    def __init__(self, color):
        self.color = color

    def action(self):
        if self.color == 'red':
            print('Stop & wait')
        elif self.color == 'yellow':
            print('Prepare to stop')
        elif self.color == 'green':
            print('Go')
        else:
            print('Stop drinking')

n = input()
st = Light(n)
st.action()


class Employee:
    def work(self):
        print("Employee works")



class Student:
    def study(self):
        print("Student studies")

class IDCard:
    def game(self):
        print("22B030628")

class WorkingStudent(Employee, Student, IDCard):  # Наследование от классов Employee и Student
    pass


# класс работающего студента

WorkingStudent().work()  # Employee works
WorkingStudent().study()  # Student studies
WorkingStudent().game()

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def shift(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return (dx ** 2 + dy ** 2)

    def __str__(self):
        return f"Point({self.x}, {self.y})"


point1 = Point(10, 4)
point2 = Point(5, 12)

print(point1.distance(point2))
point1.shift(10, 1)

print(point1.distance(point2))
print(point2.__str__())


