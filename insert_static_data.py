from database import Database

db = Database()
# Insert Counties data
counties = [
    ("C001", "Mombasa"),
    ("C002", "Kwale"),
    ("C003", "Kilifi"),
    ("C004", "Lamu"),
    ("C005", "Tana River"),
    ("C006", "Taita Taveta")
]

db.cursor.executemany("""

INSERT INTO Counties (county_id, county_name)
VALUES (?, ?)

""", counties)

# Insert Programs data
programs = [
    ("P001", "Data Analytics", 6, 120),
    ("P002", "Cybersecurity", 12, 80),
    ("P003", "Web Development", 3, 100),
    ("P004", "Software Engineering", 6, 70),
    ("P005", "AI & Prompt Engineering", 3, 90),
    ("P006", "Content Creation", 2, 60),
    ("P007", "Social Media Management", 2, 75)
]

db.cursor.executemany("""

INSERT INTO Programs
(program_id, program_name, duration_months, capacity)

VALUES (?, ?, ?, ?)

""", programs)
# Insert cohorts data
cohorts = [
    ("CH001", "May 2025", "P003", "2025-05-01", "2025-07-31"),
    ("CH002", "May 2025", "P005", "2025-05-01", "2025-07-31"),
    ("CH003", "May 2025", "P006", "2025-05-01", "2025-06-30"),
    ("CH004", "May 2025", "P007", "2025-05-01", "2025-06-30"),

    ("CH005", "October 2025", "P001", "2025-10-01", "2026-03-31"),
    ("CH006", "October 2025", "P002", "2025-10-01", "2026-09-30"),
    ("CH007", "October 2025", "P003", "2025-10-01", "2025-12-31"),
    ("CH008", "October 2025", "P004", "2025-10-01", "2026-03-31"),
    ("CH009", "October 2025", "P005", "2025-10-01", "2025-12-31"),
    ("CH010", "October 2025", "P006", "2025-10-01", "2025-11-30"),
    ("CH011", "October 2025", "P007", "2025-10-01", "2025-11-30")
]

db.cursor.executemany("""

INSERT INTO Cohorts
(cohort_id, cohort_name, program_id, start_date, end_date)

VALUES (?, ?, ?, ?, ?)

""", cohorts)



db.commit()

print("Static data inserted successfully!")

db.close()