import sqlite3
import pandas as pd
import os

# Connect to database
conn = sqlite3.connect("pwani.db")

# Folder for CSV files
output_folder = "csv_data"
os.makedirs(output_folder, exist_ok=True)

tables = [
    "Counties",
    "Programs",
    "Cohorts",
    "Applicants",
    "Applications",
    "Enrollments"
]

for table in tables:
    df = pd.read_sql_query(f"SELECT * FROM {table}", conn)
    df.to_csv(f"{output_folder}/{table}.csv", index=False)
    print(f"{table}.csv exported successfully.")

conn.close()

print("All tables exported successfully!")