# Q27. Merge two tuples and remove duplicate elements.
t1 = (1, 2, 3, 4)
t2 = (3, 4, 5, 6)

merged = tuple(set(t1 + t2))
print("Merged Tuple =", merged)
