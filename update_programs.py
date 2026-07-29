from database import Database

db = Database()

# Delete old programs
# Delete data from dependent tables
db.cursor.execute("DELETE FROM Applicants")
db.cursor.execute("DELETE FROM Cohorts")
db.cursor.execute("DELETE FROM Programs")

# New programs
programs = [
    ("P001", "STEM Cafe Kenya", 3, 120),
    ("P002", "Technovation", 4, 100),
    ("P003", "Code Hack", 3, 80),
    ("P004", "Africa Code Week", 1, 300),
    ("P005", "Django Girls", 2, 150),
    ("P006", "Mombasa Girls in STEM", 6, 60),
    ("P007", "Women Digital Skills", 2, 50),
    ("P008", "Web Development Classes", 3, 90)

]

db.cursor.executemany("""
INSERT INTO Programs
(program_id, program_name, duration_months, capacity)

VALUES (?, ?, ?, ?)
""", programs)

db.commit()

print("Programs updated successfully!")

db.close()