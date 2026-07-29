from database import Database
import random

db = Database()


# Female First Names

female_names = [
    "Amina", "Halima", "Fatma", "Aisha", "Zainab",
    "Mary", "Faith", "Mercy", "Joy", "Grace",
    "Rose", "Esther", "Caroline", "Brenda", "Diana",
    "Janet", "Naomi", "Purity", "Sharon", "Lydia",
    "Ann", "Beatrice", "Christine", "Dorcas", "Edna",
    "Eunice", "Gladys", "Hellen", "Irene", "Jackline"
]

# Male First Names

male_names = [
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


# Counties

county_ids = [
    "C001", "C002", "C003",
    "C004", "C005", "C006",
    "C007", "C008", "C009"
]

county_weights = [
    20, 10, 12,
    6, 5, 7,
    18, 12, 10
]


# Email domains

domains = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com"]
domain_weights = [70, 15, 10, 5]

# Generate Applicants

for i in range(1, 5001):

    applicant_id = f"APP{i:05d}"

    gender = random.choices(
        ["Female", "Male"],
        weights=[90, 10],
        k=1
    )[0]

    if gender == "Female":
        first_name = random.choice(female_names)
    else:
        first_name = random.choice(male_names)

    last_name = random.choice(last_names)

    # Age distribution
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

    county_id = random.choices(
        county_ids,
        weights=county_weights,
        k=1
    )[0]

    domain = random.choices(
        domains,
        weights=domain_weights,
        k=1
    )[0]

    email = f"{first_name.lower()}{last_name.lower()}{applicant_id.lower()}@{domain}"

    db.cursor.execute("""
        INSERT INTO Applicants(
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

db.commit()

print("5000 applicants generated successfully!")

db.close()