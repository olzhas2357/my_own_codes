# def greeting(name):
#   print("Hello, " + name)

# varList = ['a', 1, 'b', 2]
#
# import mymodule
#
# print(mymodule.varList)
#


person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway",
  "sex": "Man"
}
import mymodule
a = mymodule.person1["age"]
b = mymodule.person1["sex"]
print(a, b)


import mymodule as mx
a = mx.person1["age"]
print(a)

import platform
x = platform.system()
print(x)

import platform
x = dir(platform)
print(x)

