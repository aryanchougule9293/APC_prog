# 33. Take a string and use a dictionary
# to find the first character that occurs only once.

text = input("Enter a string: ")

d = {}

for i in text:
    d[i] = d.get(i, 0) + 1

for i in text:
    if d[i] == 1:
        print("First unique character:", i)
        break
