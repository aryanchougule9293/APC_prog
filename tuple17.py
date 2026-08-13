# Q17. Find largest and smallest without max() and min().
t = (5,8,2,9,1)
largest = smallest = t[0]

for i in t:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i

print("Largest =", largest)
print("Smallest =", smallest)
