class Profession:
    def __init__(self, name):
        self.name = name
    def action(self):
        if self.name == 'Coder':
            self.year = '3 year'
            print('KBTU or IT')
        elif self.name == 'Management':
            self.year = '5 year'
            print('UIB or Kimep')
        elif self.name == 'Teacher':
            self.year = '4 year'
            print('Kazguu or Abay uni')
        elif self.name == 'Doctor':
            self.year = '6 year'
            print('Asfendiyarov or KRMU')
    def where_to_work(self):
        if self.name == 'Doctor':
            self.work = "Hospital"
            print("You need to internship 2 year")
        elif self.name == 'Management':
            self.work = 'In office'
            print("You need to internship 1 year")
        elif self.name == 'Teacher':
            self.work = 'In school or University'
            print('You need to internship 0 year')
        elif self.name == 'Coder':
            self.work = 'In company'
            print('You need to internship 6 month')
print('Find out which university is better than your profession :)')
print('Coder', 'Management', 'Teacher', 'Doctor')
s = input()
k = Profession(s)
k.action()
print("This is best university in Kz")
print(f"Undergraduate will {k.year}")
print(f"When you going to work ", end = "")
k.where_to_work()


