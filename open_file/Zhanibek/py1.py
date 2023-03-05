# f = open('rawdata.txt', mode = 'w')
# print(f)
# f.write('hello kbtu\n')
# # f.close()
# f.write("1 2 3 ")
# file = open("rawdata.txt", "r")
# print(file.read())
# file.close()
#
# with open("rawdata.txt", "w") as file:
#     file.write("Your code in C++. C++ is very fast work  \n")
#
# with open("rawdata.txt", "r") as file:
#     print(file.readline())
import os

base_path = os.getcwd()
file_name = input("File name: ")
full_path = base_path + "\\" + file_name
with open(file_name, "r") as file:
    print(file.read())
n = int(input())
with open(full_path, "r+") as file:
    lines = file.readlines()
    lines[n] = input() + "\n"
    file.truncate(0)
    file.seek(0)
    file.writelines(lines)
    file.close()