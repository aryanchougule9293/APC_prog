# Q29. Convert tuple into sorted tuple.
t = (5, 2, 8, 1, 9, 3)

ascending = tuple(sorted(t))
descending = tuple(sorted(t, reverse=True))

print("Ascending :", ascending)
print("Descending:", descending)
