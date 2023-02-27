# import re
# def text_match(text):
#         patterns = '^a(b*)$'
#         if re.search(patterns,  text):
#                 return 'Found a match!'
#         else:
#                 return('Not matched!')
# print(text_match("ac"))
# print(text_match("abc"))
# print(text_match("a"))
# print(text_match("ab"))
# print(text_match("abb"))

# Функция findall() возвращает список, содержащий все совпадения.
# import re
# txt = "The rain in Spain"
# x = re.findall("Spain", txt)
# print(x)


#Функция search()ищет совпадение в строке и возвращает объект Match
# import re
# txt = "The rain in Spain"
# x = re.search("\s", txt)
# print(x.start())

#Функция split()возвращает список, в котором строка разбивается при каждом совпадении:

# import re
#
# txt = "The rain in Spain"
# x = re.split("\W", txt)
# print(x)
#
# #Функция sub()заменяет совпадения текстом по вашему выбору:
# import re
#
# txt = "The rain in Spain"
# x = re.sub("\s", "9", txt)
# print(x)

# import re
# txt = "The rain in Spain Olzhas"
# x = re.search(r"\bi\w+", txt)
# print(x.span())
# print(x.string)
# print(x.group())

#
# import re
# text = "ct"
# pattern = 'c[aoi]t'
# matching = re.search(pattern, text)
# if matching is not None:
#     print(matching)
# else:
#     print("No Match")

import re
import file

text = file.read_file('rawdata.txt')

# pattern_bin = 'БИН (?P<bin>[0-9]{12,12})'
# matching_bin = re.search(pattern_bin, text)
# if matching_bin is not None:
#     print(matching_bin.group('bin'))
# pattern_filial = 'ФИЛИАЛ (?P<filial>.*)'
# matching_filial = re.search(pattern_filial, text, re.IGNORECASE)
# print(matching_filial.group('filial'))


pattern_body = r'ПРОДАЖА(.*)Банковская карта'
matching_body = re.search(pattern_body, text, re.DOTALL)
goods = matching_body.group()

pattern_goods = r'(\d+).*\n(?P<name>.*)\n(.*) x (.*)\n'
matching_goods = re.findall(pattern_goods, goods)
print(matching_goods)

import collections
Good = collections.namedtuple('Good', ['id', 'name', 'count', 'pricePerItem'])

for good in matching_goods:
    d = Good(*good)
    print(d)






