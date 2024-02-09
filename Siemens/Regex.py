import re
s = "This is a sentence. this is a sentence"
s = re.sub(r'[^A-Za-z0-9 ]+', '', s)  # ^ says to replace anything other than A-Z, a-z, 0-9 and space
print(s)

lowers= s.lower()
print(lowers)