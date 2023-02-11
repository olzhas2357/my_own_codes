
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fact(n-1) * n

def fact_formula(n, k):
    return int(fact(n)/(fact(n-k)*fact(k)))
n = int(input())
for i in range(n):
    for j in range(i+1):
        print(fact_formula(i, j), end = " ")
    print()



