import re
def text_match(txt):
    x = re.sub("[ ,.]", ':', txt)
    return x

txt = 'olzhas is very smart, very strong and sportsman and decisive, responsible'
print(text_match(txt))