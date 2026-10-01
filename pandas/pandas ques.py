import pandas as pd

# 1. Student Marks DataFrame 
print("\n===== Question 1 =====")

students = {
    "Student ID": [101, 102, 103, 104, 105],
    "Student Name": ["Amit", "Ravi", "Sneha", "Pooja", "Kiran"],
    "Python Marks": [80, 70, 90, 60, 85],
    "DBMS Marks": [75, 65, 88, 70, 80],
    "Mathematics Marks": [85, 72, 92, 68, 78]
}

df = pd.DataFrame(students)
df["Total"] = df["Python Marks"] + df["DBMS Marks"] + df["Mathematics Marks"]
df["Average"] = df["Total"] / 3

print(df)
print("\nStudents with Average > 75")
print(df[df["Average"] > 75])

# 2. Employee DataFrame --------------------
print("\n===== Question 2 =====")

employees = {
    "Employee ID": [1, 2, 3, 4, 5],
    "Employee Name": ["Raj", "Neha", "Aman", "Priya", "Vikas"],
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "Salary": [60000, 45000, 70000, 55000, 48000],
    "Experience": [5, 3, 8, 6, 4]
}

emp = pd.DataFrame(employees)

print(emp)
print("\nSalary > 50000")
print(emp[emp["Salary"] > 50000])

print("Average Salary =", emp["Salary"].mean())
print("Highest Salary =", emp["Salary"].max())

print("\nEmployee with Highest Experience")
print(emp.loc[emp["Experience"].idxmax()])

#  3. Product DataFrame --------------------
print("\n===== Question 3 =====")

products = {
    "Product ID": [101, 102, 103, 104],
    "Product Name": ["Laptop", "Mobile", "Printer", "Tablet"],
    "Category": ["Electronics", "Electronics", "Electronics", "Electronics"],
    "Price": [50000, 20000, 15000, 30000],
    "Quantity": [2, 5, 3, 4]
}

prd = pd.DataFrame(products)
prd["Total Amount"] = prd["Price"] * prd["Quantity"]

print(prd)
print("\nProduct with Highest Total Sales")
print(prd.loc[prd["Total Amount"].idxmax()])

#  4. Patient DataFrame --------------------
print("\n===== Question 4 =====")

patients = {
    "Patient ID": [1, 2, 3, 4, 5],
    "Patient Name": ["Ram", "Shyam", "Geeta", "Mohan", "Sita"],
    "Age": [65, 45, 70, 55, 80],
    "Disease": ["Diabetes", "Fever", "Heart", "BP", "Cancer"],
    "Medical Charges": [60000, 20000, 80000, 30000, 90000]
}

pat = pd.DataFrame(patients)

print(pat)

print("\nPatients Above 60 Years")
print(pat[pat["Age"] > 60])

print("Average Medical Charge =", pat["Medical Charges"].mean())
print("Maximum Medical Charge =", pat["Medical Charges"].max())

print("\nMedical Charges > 50000")
print(pat[pat["Medical Charges"] > 50000])

#  5. Orders DataFrame --------------------
print("\n===== Question 5 =====")

orders = {
    "Order_ID": [1, 2, 3, 4],
    "Customer": ["A", "B", "C", "D"],
    "Product": ["Laptop", "Mobile", "Tablet", "Printer"],
    "Quantity": [1, 2, 1, 3],
    "Price": [50000, 20000, 30000, 15000],
    "Discount": [2000, 1000, 1500, 500]
}

ord_df = pd.DataFrame(orders)
ord_df["Final Amount"] = ord_df["Quantity"] * ord_df["Price"] - ord_df["Discount"]

print(ord_df)

print("\nOrders Above 5000")
print(ord_df[ord_df["Final Amount"] > 5000])

print("\nHighest Value Order")
print(ord_df.loc[ord_df["Final Amount"].idxmax()])

print("Average Order Value =", ord_df["Final Amount"].mean())

#  6. Attendance DataFrame --------------------
print("\n===== Question 6 =====")

attendance = {
    "Student_ID": [1, 2, 3, 4],
    "Name": ["Amit", "Ravi", "Pooja", "Sneha"],
    "Department": ["CSE", "IT", "CSE", "ECE"],
    "Total_Classes": [100, 100, 100, 100],
    "Classes_Attended": [90, 70, 80, 60]
}

att = pd.DataFrame(attendance)

att["Attendance Percentage"] = (
    att["Classes_Attended"] / att["Total_Classes"]
) * 100

print(att)

print("\nAttendance Below 75%")
print(att[att["Attendance Percentage"] < 75])

#  7. Retail Shop Sales --------------------
print("\n===== Question 7 =====")

sales = {
    "Product_ID": [1, 2, 3, 4],
    "Product_Name": ["Laptop", "Mobile", "Printer", "Tablet"],
    "Category": ["Electronics"] * 4,
    "Price": [50000, 20000, 15000, 30000],
    "Quantity": [2, 3, 4, 2]
}

sales_df = pd.DataFrame(sales)

sales_df["Total_Sales"] = sales_df["Price"] * sales_df["Quantity"]

print(sales_df)

print("\nSales > 10000")
print(sales_df[sales_df["Total_Sales"] > 10000])

print("\nMaximum Sales Product")
print(sales_df.loc[sales_df["Total_Sales"].idxmax()])

print("Average Sales =", sales_df["Total_Sales"].mean())

# 8. Student Marks Series --------------------
print("\n===== Question 8 =====")

marks = {
    "Amit": 80,
    "Ravi": 65,
    "Sneha": 90,
    "Pooja": 78
}

s = pd.Series(marks)

print(s)
print("Marks of Amit =", s["Amit"])
print("Maximum Marks =", s.max())
print("Minimum Marks =", s.min())
print("Average Marks =", s.mean())

print("\nMarks > 75")
print(s[s > 75])

# 9. Employee Salary Series --------------------
print("\n===== Question 9 =====")

salary = {
    "Raj": 60000,
    "Neha": 45000,
    "Aman": 70000,
    "Priya": 55000
}

sal = pd.Series(salary)

print(sal)
print("Highest Salary =", sal.max())
print("Lowest Salary =", sal.min())
print("Average Salary =", sal.mean())

print("\nSalary > 50000")
print(sal[sal > 50000])

# 10. Product Price Series --------------------
print("\n===== Question 10 =====")

prices = {
    "Laptop": 50000,
    "Mobile": 20000,
    "Printer": 15000,
    "Mouse": 800
}

p = pd.Series(prices)

print(p)

print("\nPrice Increased by 10%")
print(p * 1.10)

print("Most Expensive Product =", p.idxmax())

print("\nProducts Costing > 1000")
print(p[p > 1000])

# 11. Patient Age Series --------------------
print("\n===== Question 11 =====")

ages = {
    "P101": 65,
    "P102": 45,
    "P103": 70,
    "P104": 55,
    "P105": 80
}

age_series = pd.Series(ages)

print(age_series)

print("Average Age =", age_series.mean())
print("Oldest Patient =", age_series.idxmax(), age_series.max())
print("Youngest Patient =", age_series.idxmin(), age_series.min())

print("\nPatients Above 60 Years")
print(age_series[age_series > 60])

#  12. Attendance Series --------------------
print("\n===== Question 12 =====")

attendance_series = {
    "Amit": 92,
    "Ravi": 70,
    "Sneha": 96,
    "Pooja": 82,
    "Kiran": 68
}

att_ser = pd.Series(attendance_series)

print(att_ser)

print("Average Attendance =", att_ser.mean())

print("\nAttendance Below 75%")
print(att_ser[att_ser < 75])

print("\nAttendance Above 90%")
print(att_ser[att_ser > 90])

print("Highest Attendance =", att_ser.max())

# 13. students.csv --------------------
students_csv = pd.read_csv("students.csv")

print(students_csv.head())
print(students_csv.tail())

students_csv["Total"] = (
    students_csv["Python"] +
    students_csv["DBMS"] +
    students_csv["Maths"]
)

students_csv["Average"] = students_csv["Total"] / 3

print(students_csv[students_csv["Average"] > 75])

print("\nHighest Average Student")
print(students_csv.loc[students_csv["Average"].idxmax()])

print("\nSubject-wise Average")
print(students_csv[["Python", "DBMS", "Maths"]].mean())

# 14. employees.csv --------------------
emp_csv = pd.read_csv("employees.csv")

print(emp_csv[emp_csv["Department"] == "CSE"])

print("Average Salary =", emp_csv["Salary"].mean())
print("Highest Salary =", emp_csv["Salary"].max())
print("Lowest Salary =", emp_csv["Salary"].min())

print(emp_csv[emp_csv["Salary"] > 50000])

print("\nDepartment Wise Average Salary")
print(emp_csv.groupby("Department")["Salary"].mean())

# 15. patients.csv --------------------
pat_csv = pd.read_csv("patients.csv")

print(pat_csv[pat_csv["Age"] > 60])

print("Average Medical Expense =", pat_csv["Medical_Expense"].mean())

print("\nHighest Medical Expense Patient")
print(pat_csv.loc[pat_csv["Medical_Expense"].idxmax()])

print("\nDisease Count")
print(pat_csv["Disease"].value_counts())

print(pat_csv[pat_csv["Medical_Expense"] > 50000])

#  16. weather.csv --------------------
weather = pd.read_csv("weather.csv")

print("Maximum Temperature =", weather["Temperature"].max())
print("Minimum Temperature =", weather["Temperature"].min())
print("Average Temperature =", weather["Temperature"].mean())

print(weather[weather["Temperature"] > 35])

print("\nCity Wise Average Temperature")
print(weather.groupby("City")["Temperature"].mean())