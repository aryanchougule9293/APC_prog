# Q28. Count frequency of each element in a tuple.
t = (1, 2, 2, 3, 3, 3, 4, 4, 5)

for item in set(t):
    print(item, "appears", t.count(item), "times")
