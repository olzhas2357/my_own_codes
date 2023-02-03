def is_password_good(let):
    if len(let) < 8:
        return False
    flag1 = False
    flag2 = False
    flag3 = False
    for n in let:
        if n.isupper():
            flag1 = True
        elif n.islower():
            flag2 = True
        elif n.isdigit():
            flag3 = True
    return flag1 and flag2 and flag3

n = input()
print(is_password_good(n))
