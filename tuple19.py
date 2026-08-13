# Q19. Count even and odd numbers.
t = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
even = odd = 0

for i in t:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even =", even)
print("Odd =", odd)
