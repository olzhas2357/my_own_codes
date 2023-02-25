import re
txt = "ImportYouLearnEnglish"
x = re.sub(r"(\w)([A-Z])", r"\1 \2", txt)
print(x)