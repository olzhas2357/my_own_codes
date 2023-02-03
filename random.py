import random
for _ in range(10):
    print(random.randint(1, 100))

import random
num = random.randrange(10)

import random
num = random.random()
print(num)

import random
num = random.uniform(1.5, 17.3)
print(num)

import random

random.seed(17)   # явно устанавливаем начальное значение для генератора случайных чисел

for _ in range(10):
    print(random.randint(1, 100))

# Return random integer in range [a, b], including both end points.
def randint(self, a, b):
    return self.randrange(a, b + 1)

import random

print('Бросаем кубики... ')
print('Значения граней:')
print(random.randint(1, 6))
print(random.randint(1, 6))


import random

again = 'д'
while again.lower() == 'д':
    print('Бросаем кубики... ')
    print('Значения граней:')
    print(random.randint(1, 6))
    print(random.randint(1, 6))
    again = input('Бросить кубики еще раз? (д = да, н = нет): ')

import random

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(numbers)
print(numbers)

import random

print(random.choice('BEEGEEK'))
print(random.choice([1, 2, 3, 4]))
print(random.choice(['a', 'b', 'c', 'd']))

import random

numbers = [2, 5, 8, 9, 12]

print(random.sample(numbers, 1))
print(random.sample(numbers, 2))
print(random.sample(numbers, 3))
print(random.sample(numbers, 5))