# Q8. Write a Python program that stores the given details using variables: Basic Salary = ₹58,750, HRA = 22% of Basic Salary, DA = 15% of Basic Salary, Professional Tax = ₹2,500. Calculate Gross Salary, Net Salary after deducting Professional Tax, print all values using formatted print statements, print the data type of Net Salary, and round Net Salary to two decimal places.


basic_salary = 58750
hra = basic_salary * 0.22
da = basic_salary * 0.15
professional_tax = 2500

gross_salary = basic_salary + hra + da
net_salary = gross_salary - professional_tax

print("Basic Salary is:", basic_salary)
print("HRA is:", hra)
print("DA is:", da)
print("Professional Tax is:", professional_tax)
print("Gross Salary is:", gross_salary)
print("Net Salary is:", net_salary)
print("Data Type of Net Salary is:", type(net_salary))
print("Net Salary rounded to 2 decimal places:", round(net_salary, 2))