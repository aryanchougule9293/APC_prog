# 19. Create a dictionary containing duplicate values
# and remove duplicate values while retaining the corresponding keys.

d = {
    "a": 10,
    "b": 20,
    "c": 10,
    "d": 30,
    "e": 20
}

new = {}

for key, value in d.items():
    if value not in new.values():
        new[key] = value

print(new)
