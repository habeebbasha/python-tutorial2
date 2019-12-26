import re
str="abdhul kalaam178 is a *great and talented person"
s=re.findall("\b+",str)
print(s)