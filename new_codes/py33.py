def quick_merge():
    l = []
    for i in range(int(input())):
        l.extend([int(num) for num in input().split()])
    s = sorted(l)
    print(*s)

if __name__== "__main__":
    quick_merge()

# объявление функции
def is_prime(num):
    ok = True
    if num == 1:
        ok = False
    else:
        for i in range(2, num - 1):
            if num % i == 0:
                ok = False
                break
    if ok:
        return "True"
    else:
        return "False"

n = int(input())

print(is_prime(n))