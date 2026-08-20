# 35. Accept a paragraph and create a dictionary where:
# Key = word length
# Value = number of words having that length.

paragraph = input("Enter a paragraph: ")

words = paragraph.split()
d = {}

for word in words:
    length = len(word)
    d[length] = d.get(length, 0) + 1

print(d)
