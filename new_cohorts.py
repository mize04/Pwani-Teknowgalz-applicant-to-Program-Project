from database import Database

db = Database()
cohorts = [
    ("CH001", "P001", "STEM Cafe Kenya - May 2025", "2025-05-01", "2025-07-31"),
    ("CH002", "P001", "STEM Cafe Kenya - October 2025", "2025-10-01", "2025-12-31"),

    ("CH003", "P002", "Technovation - May 2025", "2025-05-01", "2025-08-31"),
    ("CH004", "P002", "Technovation - October 2025", "2025-10-01", "2026-01-31"),

    ("CH005", "P003", "Code Hack - May 2025", "2025-05-01", "2025-07-31"),
    ("CH006", "P003", "Code Hack - October 2025", "2025-10-01", "2025-12-31"),

    ("CH007", "P004", "Africa Code Week - May 2025", "2025-05-01", "2025-05-31"),
    ("CH008", "P004", "Africa Code Week - October 2025", "2025-10-01", "2025-10-31"),

    ("CH009", "P005", "Django Girls - May 2025", "2025-05-01", "2025-06-30"),
    ("CH010", "P005", "Django Girls - October 2025", "2025-10-01", "2025-11-30"),

    ("CH011", "P006", "Mombasa Girls in STEM - May 2025", "2025-05-01", "2025-10-31"),
    ("CH012", "P006", "Mombasa Girls in STEM - October 2025", "2025-10-01", "2026-03-31"),

    ("CH013", "P007", "Women Digital Skills - May 2025", "2025-05-01", "2025-06-30"),
    ("CH014", "P007", "Women Digital Skills - October 2025", "2025-10-01", "2025-11-30"),

    ("CH015", "P008", "Web Development Classes - May 2025", "2025-05-01", "2025-07-31"),
    ("CH016", "P008", "Web Development Classes - October 2025", "2025-10-01", "2025-12-31")
]
db.cursor.executemany("""
INSERT INTO Cohorts (
    cohort_id,
    program_id,
    cohort_name,
    start_date,
    end_date
)
VALUES (?, ?, ?, ?, ?)
""", cohorts)

db.commit()

print("Cohorts inserted successfully!")

db.close()