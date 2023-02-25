#CamelCase -> snake_case
from re import sub
def snake_case(s):
    return '-'.join(
        sub('([A-Z][a-z]+)', r' \1',
        sub('([A-Z]+)', r' \1',
        s.replace('_', ' ')
            )
        )
    .split()).lower()
s = input()
print(snake_case(s))
