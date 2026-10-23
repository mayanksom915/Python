import pandas as pd
print("The PANDAS Library Version: ",pd.__version__)     # 3.0.6

data = {
    "Name": ["John", "Max", "Som", "Daneil"],
    "Age": [20,21,22,23],
    "City": ["New York", "London", "Qatar", "Chicago"] 
}
df = pd.DataFrame(data)
df.index = pd.Index(["Row1", "Row2", "Row3", "Row4"])
print(df)

import pandas as pd

# 1. Create DataFrame

data = {
'Name': ['Aman', 'Ravi', 'Neha', 'Priya', 'Rahul'],
'Age': [20, 21, 19, 20, 22],
'City': ['Delhi', 'Meerut', 'Noida', 'Delhi', 'Meerut'],
'Marks': [85, 65, 92, 75, 55]
}

df = pd.DataFrame(data)

print("----- Complete Data -----")
print(df)

# 2. Show First 5 Rows

print("\n----- First 5 Rows -----")
print(df.head())

# 3. Show Data Information

print("\n----- Data Information -----")
df.info()

# 4. Show Rows and Columns

print("\n----- Shape -----")
print(df.shape)

# 5. Show Column Names

print("\n----- Column Names -----")
print(df.columns)

# 6. Select One Column

print("\n----- Student Names -----")
print(df['Name'])

# 7. Filter Students with Marks Above 70

print("\n----- Marks Above 70 -----")
print(df[df['Marks'] > 70])

# 8. Calculate Average Marks

print("\n----- Average Marks -----")
print(df['Marks'].mean())

# 9. Find Highest Marks

print("\n----- Highest Marks -----")
print(df['Marks'].max())

# 10. Find Lowest Marks

print("\n----- Lowest Marks -----")
print(df['Marks'].min())

# 11. Sort by Marks

print("\n----- Sorted by Marks -----")
print(df.sort_values('Marks', ascending=False))

# 12. Count Students in Each City

print("\n----- Students by City -----")
print(df['City'].value_counts())

# 13. Check Missing Values

print("\n----- Missing Values -----")
print(df.isnull().sum())

# 14. Add a New Column

df['Result'] = df['Marks'].apply(
lambda marks: 'Pass' if marks >= 40 else 'Fail'
)

print("\n----- Result Column Added -----")
print(df)

# 15. Group Students by City and Calculate Average Marks

print("\n----- Average Marks by City -----")
print(df.groupby('City')['Marks'].mean())

# 16. Save Data to CSV

df.to_csv('student_results.csv', index=False)

print("\nData saved to student_results.csv")

