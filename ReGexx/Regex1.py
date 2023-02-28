import re
def text_match(txt):
    patterns = '^ab+'
    if re.search(patterns, txt):
        return "Found a match"
    else:
        return "Not mathced"

txt = input()
print(text_match(txt))

import re
m = input()
patterns = '^a.*b$'
k = re.match(patterns, m)
if k:
    print("Bro GOOD")
else:
    print("Fuck you")