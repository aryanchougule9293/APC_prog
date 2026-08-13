# Q13. Modify tuple using list conversion.
t = (1,2,3)
lst = list(t)
lst[1] = 20
t = tuple(lst)
print(t)
