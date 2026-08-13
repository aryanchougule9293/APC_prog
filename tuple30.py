# Q30. Patient records operations.
patients = (
    (101, "Amit", 25, "A+"),
    (102, "Rahul", 30, "B+"),
    (103, "Sneha", 28, "A+")
)

print("All Records:")
for p in patients:
    print(p)

pid = int(input("Enter Patient ID to search: "))
found = False

for p in patients:
    if p[0] == pid:
        print("Patient Found:", p)
        found = True

if not found:
    print("Patient Not Found")

print("Total Patients =", len(patients))

bg = input("Enter Blood Group: ")
print("Patients with", bg)

for p in patients:
    if p[3] == bg:
        print(p)
