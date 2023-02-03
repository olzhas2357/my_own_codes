
def convert_to_python_case(c):
    s = ""
    for i in range(len(c)):
        if "A"<=c[i]<="Z":
            s +="_" + c[i].lower()
        else:
            s+= c[i]

    return s[1:]
c = input()
print(convert_to_python_case(c))


def convert_to_python_case(text):
    s = ''
    for el in text:
        if el.isupper():
            s += '_'
        s += el.lower()
    return s[1:]


print(convert_to_python_case(input()))