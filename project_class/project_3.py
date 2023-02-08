class WeatherCondition:
    def __init__(self, weather, temp, wear):
        self.temp = temp
    def what_to_wear(self):

#1
class Sunny(WeatherCondition):
    def __str__(self):

    def what_to_wear(self):

#2
class Cloudy(WeatherCondition):
    def __str__(self):

    def what_to_wear(self):

#3
class Rainy(WeatherCondition):
    def __str__(self):

    def what_to_wear(self):

condition = [Sunny(20), Cloudy(1), Rainy(10), Sunny(14), Cloudy(-20), Rainy(5)]
for i in condition:
