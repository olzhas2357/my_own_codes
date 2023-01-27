s = input()
s2f = s.find("f", s.find("f") + 1, len(s))
if s.count("f") == 0:
    print(-2)
elif s.count("f") == 1:
    print(-1)
else:
    print(s2f)