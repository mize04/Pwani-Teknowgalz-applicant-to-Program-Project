from database import Database
import random
from datetime import datetime, timedelta

db = Database()

# Get all enrolled applications

db.cursor.execute("""
SELECT application_id, application_date
FROM Applications
WHERE application_status = 'Enrolled'
ORDER BY application_id
""")

applications = db.cursor.fetchall()


# Generate enrollments

for i, (application_id, application_date) in enumerate(applications, start=1):

    enrollment_id = f"ENR{i:05d}"

    application_date = datetime.strptime(
        application_date,
        "%Y-%m-%d"
    )

    year = application_date.year
    month = application_date.month

    
    # Determine cohort
   

    if year == 2024 and month <= 4:

        cohort_id = "CH001"

        start = datetime(2024, 4, 25)
        end = datetime(2024, 5, 10)

    elif year == 2024:

        cohort_id = "CH002"

        start = datetime(2024, 9, 25)
        end = datetime(2024, 10, 10)

    elif year == 2025 and month <= 4:

        cohort_id = "CH003"

        start = datetime(2025, 4, 25)
        end = datetime(2025, 5, 10)

    else:

        cohort_id = "CH004"

        start = datetime(2025, 9, 25)
        end = datetime(2025, 10, 10)

    
    # Enrollment date
    

    enrollment_date = (
        start +
        timedelta(
            days=random.randint(
                0,
                (end - start).days
            )
        )
    ).strftime("%Y-%m-%d")

  
    # Completion status
    

    completion_status = random.choices(

        [
            "Completed",
            "Ongoing",
        ],

        weights=[80, 20],

        k=1

    )[0]

    
    # Insert record
    

    db.cursor.execute("""
    INSERT INTO Enrollments
    (
        enrollment_id,
        application_id,
        cohort_id,
        enrollment_date,
        completion_status
    )
    VALUES (?, ?, ?, ?, ?)
    """,
    (
        enrollment_id,
        application_id,
        cohort_id,
        enrollment_date,
        completion_status
    ))

db.commit()

print(f"{len(applications)} enrollment records generated successfully!")

db.close()