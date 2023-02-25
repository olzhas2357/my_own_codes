#snake_case -> snakeCase

import re

def snake_to_canel(word):
    return ''.join(i.capitalize() or '_' for i in word.split('_'))

word = input()
print(snake_to_canel(word))