# 8. Create a dictionary and display all keys, all values and all key-value pairs.

student = {
    "name": "Amit",
    "age": 20,
    "department": "Computer",
    "marks": 85
}

print("Keys:", student.keys())
print("Values:", student.values())
print("Key-value pairs:")

for key, value in student.items():
    print(key, ":", value)
