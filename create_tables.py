from database import Database

db = Database()
db.cursor.execute("""

CREATE TABLE IF NOT EXISTS Counties (

    county_id TEXT PRIMARY KEY,

    county_name TEXT NOT NULL

)
""")



# Create programs table
db.cursor.execute("""

CREATE TABLE IF NOT EXISTS Programs (

    program_id TEXT PRIMARY KEY,

    program_name TEXT NOT NULL,

    duration_months INTEGER NOT NULL,

    capacity INTEGER NOT NULL

);

""")
# Cohorts Table
db.cursor.execute("""

CREATE TABLE IF NOT EXISTS Cohorts (

    cohort_id TEXT PRIMARY KEY,

    cohort_name TEXT NOT NULL,

    program_id TEXT NOT NULL,

    start_date DATE NOT NULL,

    end_date DATE NOT NULL,

    FOREIGN KEY (program_id)
        REFERENCES Programs(program_id)

);

""")

# Applicants Table
db.cursor.execute("""

CREATE TABLE IF NOT EXISTS Applicants (

    applicant_id TEXT PRIMARY KEY,

    first_name TEXT NOT NULL,

    last_name TEXT NOT NULL,

    age INTEGER NOT NULL,

    gender TEXT NOT NULL,

    county_id TEXT NOT NULL,

    education_level TEXT NOT NULL,

    email TEXT UNIQUE NOT NULL,

    FOREIGN KEY (county_id)
        REFERENCES Counties(county_id)

);

""")

# Applications Table
db.cursor.execute("""

CREATE TABLE IF NOT EXISTS Applications (

    application_id TEXT PRIMARY KEY,

    applicant_id TEXT NOT NULL,

    program_id TEXT NOT NULL,

    application_date DATE NOT NULL,

    application_status TEXT NOT NULL,

    drop_off_reason TEXT,

    FOREIGN KEY (applicant_id)
        REFERENCES Applicants(applicant_id),

    FOREIGN KEY (program_id)
        REFERENCES Programs(program_id)

);

""")
# Enrollments Table
db.cursor.execute("""

CREATE TABLE IF NOT EXISTS Enrollments (

    enrollment_id TEXT PRIMARY KEY,

    application_id TEXT NOT NULL,

    cohort_id TEXT NOT NULL,

    enrollment_date DATE NOT NULL,

    completion_status TEXT NOT NULL,

    FOREIGN KEY (application_id)
        REFERENCES Applications(application_id),

    FOREIGN KEY (cohort_id)
        REFERENCES Cohorts(cohort_id)

);

""")
db.commit()

db.close()

print("6 tables created successfully!")