__author__ = 'Baka'

import os

os.getcwd()
os.chdir('../text')

print(os.getcwd())

# data = open('sketch.txt')
# print(data.readline(), end='')
# data.seek(0)
# for each_line in data:
#     print(each_line, end='')
#
# data.close()

newstring = 'Man: Is this the right room for an argument?'
(role, spoken) = newstring.split(":")

print()
# print(role, end='')
# print(" said: ", end='')
# print(spoken, end='')

import sys
print (sys.version)

#
# movies = ["Harry Potter", "Lord of the rings"]
#
# # for m in movies:
# #     print(m)
#
#
#
# def print_all(the_list):
#     for i in the_list:
#         if isinstance(i, list):
#             print_all(i)
#         else:
#             print(i)
#
# print_all(movies)


# print(movies[0])
# print("Hello, World!")
