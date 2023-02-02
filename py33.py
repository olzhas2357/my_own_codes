def quick_merge():
    l = []
    for i in range(int(input())):
        l.extend([int(num) for num in input().split()])
    s = sorted(l)
    print(*s)

if __name__== "__main__":
    quick_merge()