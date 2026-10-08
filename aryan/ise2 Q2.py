import pandas as pd

data = {
    "Name": ["Amit", "Rahul", "Priya", "Sneha"],
    "Department": ["IT", "HR", "IT", "HR"],
    "Salary": [50000, 40000, 60000, 45000]
}

df = pd.DataFrame(data)

def salary_analysis(df):
    print("Highest Paid Employee:")
    print(df.loc[df["Salary"].idxmax()])

    print("\nDepartment-wise Average Salary:")
    print(df.groupby("Department")["Salary"].mean())

    df["Rank"] = df["Salary"].rank(ascending=False)
    print("\nSalary Ranking:")
    print(df.sort_values("Rank"))

salary_analysis(df)