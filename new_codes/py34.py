def prime(c):
    ok = True
    if int(c) == 1:
        ok = False
    for i in range(2, int(c)):
        if int(c) % i == 0:
            ok = False
            break
        ok = True
    return ok

def is_valid_password(s):
    l = s.split(":")
    if len(l) == 3:
        if l[0] == l[0][::-1] and prime(l[1]) and int(l[2]) % 2 == 0:
            return True
        else:
            return False
    else:
        return False
s = input()
print(is_valid_password(s))