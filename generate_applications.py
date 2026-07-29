from database import Database
import random
from datetime import datetime, timedelta

db = Database()

# Fetch applicants

db.cursor.execute("""
SELECT applicant_id, gender
FROM Applicants
ORDER BY applicant_id
""")

applicants = db.cursor.fetchall()


# Program IDs

program_ids = [
    "P001",
    "P002",
    "P003",
    "P004",
    "P005",
    "P006",
    "P007",
    "P008"
]

# More popular programs receive more applications
program_weights = [
    18, 16, 12, 22,
    10, 7, 6, 9
]

# Female funnel


female_count = sum(
    1 for _, gender in applicants
    if gender == "Female"
)

applied = int(female_count * 0.34)
qualified = int(female_count * 0.33)
interviewed = int(female_count * 0.17)
enrolled = female_count - (
    applied +
    qualified +
    interviewed
)

female_statuses = (
    ["Applied"] * applied +
    ["Qualified"] * qualified +
    ["Interviewed"] * interviewed +
    ["Enrolled"] * enrolled
)

random.shuffle(female_statuses)

female_index = 0


# Drop-off reasons


applied_reasons = [
    "Incomplete Application",
    "Did Not Meet Requirements"
]

qualified_reasons = [
    "Could Not Be Reached",
    "No Response",
    "Interview Slots Full"
]

interviewed_reasons = [
    "Low Interview Score",
    "Declined Offer",
    "Cohort Full"
]


# Generate records


for i, (applicant_id, gender) in enumerate(applicants, start=1):

    application_id = f"APL{i:05d}"

    program_id = random.choices(
        program_ids,
        weights=program_weights,
        k=1
    )[0]

    
    # Generate application date
    

    intake = random.choice([
        "May2024",
        "Oct2024",
        "May2025",
        "Oct2025"
    ])

    if intake == "May2024":

        start = datetime(2024, 1, 1)
        end = datetime(2024, 4, 30)

    elif intake == "Oct2024":

        start = datetime(2024, 6, 1)
        end = datetime(2024, 9, 30)

    elif intake == "May2025":

        start = datetime(2025, 1, 1)
        end = datetime(2025, 4, 30)

    else:

        start = datetime(2025, 6, 1)
        end = datetime(2025, 9, 30)

    days = (end - start).days

    application_date = (
        start +
        timedelta(days=random.randint(0, days))
    ).strftime("%Y-%m-%d")

    
    # Male applicants


    if gender == "Male":

        application_status = "Applied"
        drop_off_reason = "Gender Mismatch"

    
    # Female applicants
    

    else:

        application_status = female_statuses[female_index]
        female_index += 1

        if application_status == "Applied":

            drop_off_reason = random.choice(
                applied_reasons
            )

        elif application_status == "Qualified":

            drop_off_reason = random.choice(
                qualified_reasons
            )

        elif application_status == "Interviewed":

            drop_off_reason = random.choice(
                interviewed_reasons
            )

        else:

            drop_off_reason = None

    db.cursor.execute("""
    INSERT INTO Applications
    (
        application_id,
        applicant_id,
        program_id,
        application_date,
        application_status,
        drop_off_reason
    )
    VALUES (?, ?, ?, ?, ?, ?)
    """,
    (
        application_id,
        applicant_id,
        program_id,
        application_date,
        application_status,
        drop_off_reason
    ))

db.commit()

print("5000 application records generated successfully!")

db.close()