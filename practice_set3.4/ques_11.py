rdec_departments = {
    "CSE": {"HOD Name": "Dr. A. Sharma", "Number of Faculty": 45, "Number of Students": 480},
    "ECE": {"HOD Name": "Dr. B. Verma", "Number of Faculty": 30, "Number of Students": 320},
    "ME": {"HOD Name": "Dr. C. Singh", "Number of Faculty": 25, "Number of Students": 200}
}

# 1. Print the HOD of the ECE department
print("1. HOD of ECE:", rdec_departments["ECE"]["HOD Name"])

# 2. Print the number of students in the CSE department
print("2. Number of students in CSE:", rdec_departments["CSE"]["Number of Students"])

# 3. Update the faculty count of the ME department
rdec_departments["ME"]["Number of Faculty"] = 28
print("3. Updated ME faculty count.")

# 4. Add a new department named Civil
rdec_departments["Civil"] = {"HOD Name": "Dr. D. Pal", "Number of Faculty": 15, "Number of Students": 120}
print("4. Added Civil department.")

# 5. Print all department names
print("5. Department Names:")
for dept in rdec_departments:
    print("-", dept)

# 6. Print the complete nested dictionary
print("\n6. Complete Department Dictionary:")
print(rdec_departments)


# output:
# 1. HOD of ECE: Dr. B. Verma
# 2. Number of students in CSE: 480
# 3. Updated ME faculty count.
# 4. Added Civil department.
# 5. Department Names:
# - CSE
# - ECE
# - ME
# - Civil
# 6. Complete Department Dictionary:
# {'CSE': {'HOD Name': 'Dr. A. Sharma', 'Number of Faculty': 45, 'Number of Students': 480}, 'ECE': {'HOD Name': 'Dr. B. Verma', 'Number of Faculty': 30, 'Number of Students': 320}, 'ME': {'HOD Name': 'Dr. C. Singh', 'Number of Faculty': 28, 'Number of Students': 200}, 'Civil': {'HOD Name': 'Dr. D. Pal', 'Number of Faculty': 15, 'Number of Students': 120}}