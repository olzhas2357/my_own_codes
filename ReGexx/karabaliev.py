# # Task 1
# import re
# # string = 'his olzhaskoshkarbay@gmail.com'
#
# string1 = input("Пишите тут: ")
# pattern = '^.*@+[a-z]+.+org$'
# # txt = re.search(pattern, string)
# txt1 = re.findall(pattern, string1)
# print('Ok', txt1)

#patterns = '\Bz\B' не началу и не в концу

# import re
#
# string = input()
#
# regex = re.sub('\.[0]*', '.', string)
# print(regex)
#
#

# import re
# string = input()
# text = re.compile(r".*[0-9]$")
# if text.match(string):
#     print(True)
# else:
    # print(False)


import re
#
# def extract_emails(text):
#     pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
#     emails = re.findall(pattern, text)
#     return emails
#
# text = input()
# emails = extract_emails(text)
# print(emails) # Output: ['john.doe@example.com', 'jane@example.com']
#
