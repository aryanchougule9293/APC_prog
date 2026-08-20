# 16. Create two dictionaries and merge them into a single dictionary.

d1 = {
    "a": 10,
    "b": 20
}

d2 = {
    "c": 30,
    "d": 40
}

d1.update(d2)

print(d1)
