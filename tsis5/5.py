#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

import re
txt = input()

x = re.match('a.*?b$', txt)

print(x)