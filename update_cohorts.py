from database import Database
db= Database()

# Delete old cohorts
db.cursor.execute("DELETE FROM Cohorts") 

# Insert Cohorts data
cohorts = [
    ("CH001", "May 2024", "P003", "2024-05-01", "2024-07-31"),
    ("CH002", "May 2024", "P005", "2024-05-01", "2024-07-31"),
    ("CH003", "May 2024", "P006", "2024-05-01", "2024-06-30"),
    ("CH004", "May 2024", "P007", "2024-05-01", "2024-06-30"),
    ("CH005", "October 2024", "P001", "2024-10-01", "2025-03-31"),
    ("CH006", "October 2024", "P002", "2024-10-01", "2025-09-30"),
    ("CH007", "October 2024", "P004", "2024-10-01", "2025-12-31"),

    ("CH008", "May 2025", "P004", "2025-05-01", "2026-11-31"),
    ("CH009", "May 2025", "P005", "2025-05-01", "2025-07-31"),
    ("CH010", "May 2025", "P006", "2025-05-01", "2025-06-30"),
    ("CH011", "May 2025", "P007", "2025-05-01", "2025-06-30"),
    ("CH012", "October 2025", "P001", "2025-10-01", "2026-03-31"),
    ("CH013", "October 2025", "P002", "2025-10-01", "2026-09-30"),
    ("CH014", "October 2025", "P003", "2025-10-01", "2025-12-31")
]

db.cursor.executemany("""

INSERT INTO Cohorts
(cohort_id, cohort_name, program_id, start_date, end_date)

VALUES (?, ?, ?, ?, ?)

""", cohorts)
db.commit()

print("Cohorts updated successfully!")
db.close()