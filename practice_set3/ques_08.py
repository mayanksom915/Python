basic_salary = 75800
hra = basic_salary * 0.22
professional_tax = 2500
gross_salary = basic_salary + hra
net_salary = gross_salary - professional_tax

print("Gross Salary is:", gross_salary)
print("HRA :", hra)
print("professional tax: ",professional_tax)
print("Gross Salary is:", gross_salary)
print("Net Salary is:", net_salary)
print("Data Type of Net Salary is:", type(net_salary))