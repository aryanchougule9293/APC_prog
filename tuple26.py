# Q26. Find common elements between two tuples.
t1 = (1, 2, 3, 4, 5)
t2 = (4, 5, 6, 7, 8)

common = tuple(set(t1) & set(t2))
print("Common Elements =", common)
