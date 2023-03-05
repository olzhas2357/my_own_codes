import os

# path = input()
# os.path.exists(path)
# for i in os.listdir():
#         print(i)

# 2
# n = input()
# f = open(n, 'r')
# content = f.read()
# print(content)
# print(len(content))
# print(content.count('def '))
# print(content.count('='))

# import os
# base_path = os.getcwd()
# file_name = input("File name: ")
#
# full_path = base_path + "\\" + file_name
#
# with open(full_path, 'r') as file:
#     file_data = file.read()
#     print(file_data)
# n = int(input())
# with open(full_path, 'r+') as file:
#     lines = file.readlines()
#     lines[n] = input()+"\n"
#     file.truncate(0)
#     file.seek(0)
#     file.writelines(lines)

# with open("rawdata2.txt", "w+") as f:
#     f.write("test_1\n")
#     f.write("test_22\n")
#     f.write("test_562\n")
#     f.seek(0)
#     lines = f.read()
#     print(lines)
#
# with open("rawdata2.txt", 'a+') as f:
#     f.seek(0)
#     lines = f.readlines()
#     f.write("\n" + str(len(lines)) + "\n" )
#
# with open('rawdata2.txt', 'a') as f:
#     f.write("test_123\n")
#     f.write("test_54")
#
# f = open("rawdata2.txt", "w+")
# print(f.read())

# import os
#
# k = os.getcwd()
# print(k)

# import os
# import sys
#
# path1 = os.access("rawdata.txt", os.F_OK)
# print("Exists the path:", path1)
#
# path2 = os.access("rawdata.txt", os.R_OK)
# print("Access to read the file:", path2)
#
# path3 = os.access("rawdata.txt", os.W_OK)
# print("Access to write the file:", path3)
#
# path4 = os.access("rawdata.txt", os.X_OK)
# print(path4)

# with open("rawdata.txt", "a") as f:
#     f.writelines(["map<int, int> m;"])
#
# with open("rawdata.txt", "r") as f:
#     print(f.read())

import os
directory = "new_file"
parent_dir = os.path.abspath("AREN")
path = os.path.join(parent_dir, directory)

os.makedirs(path)
print("Director '%s' created" %directory)