import re

txt = input()

x = re.findall(r'\bc\w*t\b', txt)

print(x)