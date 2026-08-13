# Q12. Accept five numbers and convert list to tuple.
lst = []
for i in range(5):
    lst.append(int(input("Enter number: ")))
t = tuple(lst)
print(t)
