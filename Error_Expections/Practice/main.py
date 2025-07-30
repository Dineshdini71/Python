# FileNotFoundError
# with open('a_file.txt', 'r') as file:
#     print(file)
from fileinput import close
from fnmatch import fnmatch
from tkinter import EXCEPTION

# KeyError
# dict = {'key': 'value'}
# print(dict["dinesh"])

# IndexError
# dup = ['Apple','Ball', 'cat']
# print(dup[3])

# TypeError
# a = 23 + '5'
# print(a)

# ----------------------- EXCEPTIONS -----------------------

# 1. try
# 2. except
# 3. else
# 4. finally

# -----------------------------------------------------------

# try:
#     file = open('b_file.txt')
#     b_dict = {'key': 'dinesh'}
#     print(b_dict['key'])
# except FileNotFoundError:
#     file = open('b_file.txt', 'w')
#     file.write('I am writing in except')
# except KeyError as e:
#     print(f"This key {e} id doesn't exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is an error which I made UP")

# -----------------------------------------------------------

# ------------------- RAISE OWN EXCEPTION -------------------

height = float(input("Height: " ))
weight = int(input("Weight: " ))

if height > 3:
    raise ValueError("Human height is not greater than 3 meters...")

bmi = weight / height ** 2

print(bmi)

# ------------------- HOW IT WILL WORK -------------------

# try:
#
#       It means, If issue is occurs or fails the block of code.
#
# expect:
#
#       This block of code is deals or resolve the issue.
#
# else:
#
#        If try block runs without occur any issue. This block of code will be execute
#
# finally:
#
#        This code will be execute, Above all exceptions are will be success.







































