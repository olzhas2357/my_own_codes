# class Holiday:
#     def __init__(self, place, time):
#         self.time = time
#         self.place = place
#     def where_and_time(self):
#         print(f"I`m going to travel {self.place} I will there during {self.time} ")
# r1 = Holiday("Hawaii", "3 month")
# r1.where_and_time()
# class Sunny(Holiday):
#     def __init__(self, place, time, wear, pl, hotel):
#         super().__init__(place, time)
#         self.time = time
#         self.place = place
#         self.wear = wear
#         self.inters_pl = pl
#         self.hotel = hotel
#     def preposition(self):
#         print(f"I advice you wear {self.wear} Interest place in {self.place} this {self.inters_pl} and {self.hotel}")
#
# p1 = Sunny("Hawaii", "3 month", "Short and t-shirt or dress", "Haleakala National Park and Waikiki Beach", "HOTEL HAWAII" )
# p2 = Sunny("Miami", "2 month", "Short and t-shirt or dress", "Miami Beach, Area Wynwood", "HOTEL MAIMI")
# p1.preposition()
#
#
# class Table:
#     def __init__(self, l, w, h):
#         self.length = l
#         self.width = w
#         self.height = h
#
#
# class DeskTable(Table):
#     def square(self):
#         return self.width * self.length
#
#
# t1 = Table(1.5, 1.8, 0.75)
# t2 = DeskTable(0.8, 0.6, 0.7)
# print(t2.square())  # вывод: 0.48

# class Square:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#
# class Shape(Square):
#     def __init__(self, length, width):
#         super().__init__(length, width)
#
#     def area(self, length, *width):
#         print(self.length * self.width)
#
# squa = Shape(int(input()), float(input()))
# squa.area(squa)

