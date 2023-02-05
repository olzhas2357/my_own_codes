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


def get_next_prime(num):
    num+=1
    for i in range(2, num):
        if num % i == 0:
            return get_next_prime(num)
    return num
n = int(input())
print(get_next_prime(n))


def is_correct_bracket(s):
    sum = 0
    while '()' in s:
        s = s.replace("()", "")
    if s == "":
        return True
    return False
if __name__ == "__main__":
    w = input()
    print(is_correct_bracket(w))