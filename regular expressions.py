#search method in re(this gives the result of match object t/f)
import re
str="habeeb is working on python"
x=re.search("habeeb",str)
if x:
    print("match found",x.group())
else:
    print('not matched')
y=re.search('^habeeb.*python$',str)
if y:
    print('string founded starting with habeeb and ends with python:',y.group())
else:
    print('not found')
z=re.search("\s",str)  #searching for the space index number from string
if z:
    print('matched',z.start()) #posotion of that space white-space
    print("span of that match",z.span())#first and last indexes of that match

#findall method(it returns a list containing all matches)
str1="the spain has rain today 12 A.M"
x=re.findall("ai",str1)
print(x)
y=re.findall("[a-z]",str1)
print(y)

#split method
str2="rain in spain"
y=re.split("a",str2)
print(y)

str2="rain in spain"
y=re.split("a",str2,1)

print(y)

#sub and subn methods
st="habeeb is an employ"
x=re.sub("\s","4",st)
y=re.subn("b","2",st)
print(x)
print(y)
#match and full match
s="don't be a joker"
z=re.match("don't",s)
y=re.fullmatch("don't be a joker",s)
print(y)
if z:
    print("matched")
else:
    print("not matched")

# Module Regular Expression is imported using __import__().
import re

# compile() creates regular expression character class [a-e],
# which is equivalent to [abcde].
# class [abcde] will match with string with 'a', 'b', 'c', 'd', 'e'.
p = re.compile('\w+')

# findall() searches for the Regular Expression and return a list upon finding
print(p.findall("Aye, said Mr. Gibenson Stark"))









