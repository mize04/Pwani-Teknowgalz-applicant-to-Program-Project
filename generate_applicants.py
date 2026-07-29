from database import Database
import random

# Connect to database
db = Database()

# Female First Names

first_names_female = [
    "Amina", "Halima", "Fatma", "Aisha", "Zainab",
    "Mary", "Faith", "Mercy", "Joy", "Grace",
    "Rose", "Esther", "Caroline", "Brenda", "Diana",
    "Janet", "Naomi", "Purity", "Sharon", "Lydia",
    "Ann", "Beatrice", "Christine", "Dorcas", "Edna",
    "Eunice", "Gladys", "Hellen", "Irene", "Jackline"
]

# Male First Names
first_names_male = [
    "Brian", "Kevin", "Ali", "Hassan", "Mohamed",
    "John", "Daniel", "Peter", "James", "Eric",
    "David", "Samuel", "Joseph", "Mark", "Paul",
    "Dennis", "Victor", "Emmanuel", "Collins", "Steve",
    "Kennedy", "Charles", "Kelvin", "Martin", "Patrick"
]

# Last Names

last_names = [
    "Khalfan", "Mohamed", "Ali", "Mwangi", "Otieno",
    "Kamau", "Ouma", "Mutua", "Juma", "Abdalla",
    "Omondi", "Munyao", "Kiptoo", "Wanjiku", "Maina",
    "Kariuki", "Njoroge", "Koech", "Chebet", "Rotich",
    "Barasa", "Musyoka", "Muli", "Ndungu", "Wambui",
    "Nyambura", "Odhiambo", "Makena", "Nyongesa", "Gitau"
]


# Counties (Weighted)

county_ids = ["C001", "C002", "C003", "C004", "C005", "C006"]
county_weights = [35, 18, 22, 8, 7, 10]


# Email Domains

email_domains = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com"]
email_weights = [70, 15, 10, 5]


# Generate 5000 Applicants

for i in range(1, 5001):

    # Applicant ID
    applicant_id = f"APP{i:05d}"

    # Gender (90% Female, 10% Male)
    gender = random.choices(
        ["Female", "Male"],
        weights=[90, 10],
        k=1
    )[0]

    # First Name
    if gender == "Female":
        first_name = random.choice(first_names_female)
    else:
        first_name = random.choice(first_names_male)

    # Last Name
    last_name = random.choice(last_names)

    # Age Distribution
    age_group = random.choices(
        ["18-22", "23-27", "28-35"],
        weights=[45, 35, 20],
        k=1
    )[0]

    if age_group == "18-22":
        age = random.randint(18, 22)
        education = random.choices(
            ["KCSE", "Certificate", "Diploma"],
            weights=[70, 20, 10],
            k=1
        )[0]

    elif age_group == "23-27":
        age = random.randint(23, 27)
        education = random.choices(
            ["KCSE", "Certificate", "Diploma", "Bachelor's"],
            weights=[20, 35, 35, 10],
            k=1
        )[0]

    else:
        age = random.randint(28, 35)
        education = random.choices(
            ["Diploma", "Bachelor's", "Master's"],
            weights=[25, 60, 15],
            k=1
        )[0]

    # County
    county_id = random.choices(
        county_ids,
        weights=county_weights,
        k=1
    )[0]

    # Email
    domain = random.choices(
        email_domains,
        weights=email_weights,
        k=1
    )[0]

    email = (
        f"{first_name.lower()}"
        f"{last_name.lower()}"
        f"{applicant_id.lower()}@{domain}"
    )

    # Insert Applicant
    db.cursor.execute("""
        INSERT INTO Applicants (
            applicant_id,
            first_name,
            last_name,
            age,
            gender,
            county_id,
            education_level,
            email
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        applicant_id,
        first_name,
        last_name,
        age,
        gender,
        county_id,
        education,
        email
    ))

# Save changes
db.commit()

print("5000 applications generated successfully!")

db.close()