science = {"Aman", "Riya", "Rahul", "Priya", "Ankit"}
coding = {"Rahul", "Ankit", "Simran", "Rohit", "Riya"}

# 1. Students enrolled in either club
print("Students in either club:", science | coding)

# 2. Students enrolled in both clubs
print("Students in both clubs:", science & coding)

# 3. Students only in Science Club
print("Only in Science Club:", science - coding)

# 4. Students only in Coding Club
print("Only in Coding Club:", coding - science)

# 5. Check common members
print("Common members exist:", not science.isdisjoint(coding))

# 6. Add a new student to Coding Club
coding.add("Neha")

# 7. Remove one student from Science Club
science.remove("Priya")

# 8. Print updated sets
print("Updated Science Club:", science)
print("Updated Coding Club:", coding)

# output:
# Students in either club: {'Riya', 'Ankit', 'Simran', 'Rohit', 'Aman', 'Rahul', 'Neha', 'Priya'}
# Students in both clubs: {'Riya', 'Ankit', 'Rahul'}
# Only in Science Club: {'Aman', 'Priya'}
# Only in Coding Club: {'Simran', 'Rohit'}
# Common members exist: True  
# Updated Science Club: {'Riya', 'Aman', 'Rahul', 'Ankit'}
# Updated Coding Club: {'Riya', 'Ankit', 'Simran', 'Rohit', 'Neha', 'Rahul'}  