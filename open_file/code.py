
f = open('Zhanibek/rawdata.txt', mode ='r')
s = f.readlines()
print(s)
f.close()

# with open('rawdata.txt', mode = 'r') as f:
#     print(f.readlines())

import os

# print(os.environ['PATH'])
# print(os.getenv('-------', 'olzhas'))

# print(os.getcwd())
# os.chdir('tests')
# print(os.getcwd())
#

#
# os.rmdir('./tests')
# os.mkdir('./new')


# frath = 'python.py'
#
# print(os.path.join(os.getcwd(), 'new', frath))
# if os.path.exists(frath):
#     print("del file")

# import shutil
#
# shutil.move(
#     './new',
#     './Zhanibek'
# )

# try:
#     number = 5
#     div = int(input())
#     print(number/ div)
# except ZeroDivisionError as err:
#     print("No no error", err)

#
#
# try:
#     number = 5
#     div = input()
#     if not div.isdigit():
#         raise ValueError('No no number')
#
# except (ValueError, ZeroDivisionError) as err:
#     print("без комментариев")
# else:
#     print("без ошибок")
# finally:
#     print("Finally block")



import time

print("Printed immediately.")
time.sleep(25)
print("Printed after 2.4 seconds.")
