# # PANDAS FUNCTIONS AND USES — BEGINNER LEVEL

# ## 1. PANDAS BASICS

# 1. pd.Series()
#    Use: One-dimensional data structure banana.
#    pd.Series([10, 20, 30, 40])

# 2. pd.DataFrame()
#    Use: Rows aur columns wala table banana.
#    pd.DataFrame({'Name': ['Aman', 'Ravi'], 'Age': [20, 21]})

# 3. pd.read_csv()
#    Use: CSV file ko read karna.
#    pd.read_csv('data.csv')

# 4. pd.read_excel()
#    Use: Excel file ko read karna.
#    pd.read_excel('data.xlsx')

# 5. df.to_csv()
#    Use: DataFrame ko CSV file mein save karna.
#    df.to_csv('output.csv', index=False)

# 6. df.to_excel()
#    Use: DataFrame ko Excel file mein save karna.
#    df.to_excel('output.xlsx', index=False)

# ## 2. DATA DEKHNE KE FUNCTIONS

# 7. df.head()
#    Use: Starting ki 5 rows dekhna.
#    df.head()

# 8. df.tail()
#    Use: Last ki 5 rows dekhna.
#    df.tail()

# 9. df.sample()
#    Use: Random rows dekhna.
#    df.sample(3)

# 10. df.info()
#     Use: Columns, data types aur non-null values ki information dekhna.
#     df.info()

# 11. df.describe()
#     Use: Numerical columns ki statistical summary dekhna.
#     df.describe()

# 12. df.shape
#     Use: Rows aur columns ki total sankhya dekhna.
#     df.shape

# 13. df.columns
#     Use: Sabhi column names dekhna.
#     df.columns

# 14. df.dtypes
#     Use: Har column ka data type dekhna.
#     df.dtypes

# 15. len(df)
#     Use: Total rows count karna.
#     len(df)

# ## 3. DATA SELECT KARNE KE FUNCTIONS

# 16. df['Name']
#     Use: Ek column select karna.
#     df['Name']

# 17. df[['Name', 'Age']]
#     Use: Multiple columns select karna.
#     df[['Name', 'Age']]

# 18. df.iloc[]
#     Use: Row aur column ki position ke according data select karna.
#     df.iloc[0]

# 19. df.loc[]
#     Use: Index labels ke according data select karna.
#     df.loc[0]

# 20. df['Age'].unique()
#     Use: Column ki unique values dekhna.
#     df['Age'].unique()

# 21. df['Age'].nunique()
#     Use: Unique values ki count nikalna.
#     df['Age'].nunique()

# ## 4. DATA FILTERING

# 22. df[df['Age'] > 20]
#     Use: Condition ke according rows filter karna.
#     df[df['Age'] > 20]

# 23. df[df['City'] == 'Delhi']
#     Use: Matching condition wali rows select karna.
#     df[df['City'] == 'Delhi']

# 24. df.isnull()
#     Use: Missing values check karna.
#     df.isnull()

# 25. df.isnull().sum()
#     Use: Har column mein missing values count karna.
#     df.isnull().sum()

# 26. df.notnull()
#     Use: Non-missing values check karna.
#     df.notnull()

# ## 5. DATA CLEANING

# 27. df.drop()
#     Use: Rows ya columns remove karna.
#     df.drop(columns=['Age'])

# 28. df.rename()
#     Use: Column ya index ka naam change karna.
#     df.rename(columns={'Name': 'Student'})

# 29. df.drop_duplicates()
#     Use: Duplicate rows remove karna.
#     df.drop_duplicates()

# 30. df.fillna()
#     Use: Missing values ko kisi value se fill karna.
#     df.fillna(0)

# 31. df.dropna()
#     Use: Missing values wali rows ya columns remove karna.
#     df.dropna()

# 32. df.astype()
#     Use: Column ka data type change karna.
#     df['Age'].astype(int)

# ## 6. DATA SORTING AND COUNTING

# 33. df.sort_values()
#     Use: Column ki values ke according data sort karna.
#     df.sort_values('Age')

# 34. df.value_counts()
#     Use: Values kitni baar aayi hain, unki frequency count karna.
#     df['City'].value_counts()

# 35. df['Age'].sum()
#     Use: Age column ki values ka total nikalna.
#     df['Age'].sum()

# 36. df['Age'].mean()
#     Use: Average nikalna.
#     df['Age'].mean()

# 37. df['Age'].max()
#     Use: Maximum value nikalna.
#     df['Age'].max()

# 38. df['Age'].min()
#     Use: Minimum value nikalna.
#     df['Age'].min()

# 39. df['Age'].count()
#     Use: Non-missing values count karna.
#     df['Age'].count()

# ## 7. DATA ADD AND UPDATE

# 40. df['Marks'] = [80, 90, 75]
#     Use: Naya column add karna.
#     df['Marks'] = [80, 90, 75]

# 41. df.drop(columns=['Marks'])
#     Use: Marks column remove karna.
#     df.drop(columns=['Marks'])

# 42. df['Age'] = df['Age'] + 1
#     Use: Column ki values update karna.
#     df['Age'] = df['Age'] + 1

# 43. df.replace()
#     Use: Specific values replace karna.
#     df.replace('Delhi', 'Meerut')

# ## 8. GROUPING AND COMBINING

# 44. df.groupby()
#     Use: Same category ke data ko group karna.
#     df.groupby('City')['Age'].mean()

# 45. pd.concat()
#     Use: DataFrames ko rows ya columns ke along combine karna.
#     pd.concat([df1, df2])

# 46. pd.merge()
#     Use: Common column ke through DataFrames join karna.
#     pd.merge(df1, df2, on='ID')

# ## IMPORTANT NOTES

# 1. Pandas import karne ke liye:
#    import pandas as pd

# 2. DataFrame banane ke liye:
#    df = pd.DataFrame({
#    'Name': ['Aman', 'Ravi', 'Neha'],
#    'Age': [20, 22, 19],
#    'City': ['Delhi', 'Meerut', 'Noida']
#    })

# 3. Data dekhne ke liye:
#    print(df)

# 4. Pehli 5 rows dekhne ke liye:
#    print(df.head())

# 5. Average age nikalne ke liye:
#    print(df['Age'].mean())

# 6. CSV file read karne ke liye:
#    df = pd.read_csv('data.csv')
