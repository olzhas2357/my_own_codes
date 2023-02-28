
#
# def is_allowed_specific(string):
#     char = re.compile(r'[a-zA-Z0-9]')
#     string = char.search(string)
#     return bool(string)
#
# txt = input()
# print(is_allowed_specific(txt))
import re
results = re.finditer(r"([0-9]{1,5})", "Exercises number 1, 12, 13, and 345 are important")
print("Number of length 1 to 3")
for n in results:
     print(n.group(0))