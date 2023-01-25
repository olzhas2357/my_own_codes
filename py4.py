s = input()
sum = 0
for i in range(len(s)-1):
    if s[i] == s[i+1]:
       sum += 1
print(sum)