keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']

new_keywords = [keywords[i][j] for i in range(0, len(keywords)) for j in range(1, len(keywords[i]))]

print(new_keywords)

keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']

lengths = [keywords[i] for i in range(len(keywords)) if len(keywords[i]) <= 5]

print(lengths)

palindromes = [i for i in range(100, 1000) if str(i) == str(i)[::-1]]

print(palindromes)

print(*[i**2 for i in range(1, int(input())+1)], sep = "\n")


print(*[int(i) ** 3 for i in input().split()])

print(*[num for num in input().split()],  sep="\n")

print(*[i for i in input() if i in "0123456789"], sep = "")

print(*[int(i)**2 for i in input().split() if int(i) ** 2 % 10 != 4 and int(i) % 2 == 0])