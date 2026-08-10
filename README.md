# Pwani-Teknowgalz-applicant-to-Program-Project
This project will provide an interactive dashboard maintainable by the organization staff that will enable the organization to monitor applicant journey, identify enrollment bottlenecks, understand who is being underserved, track resource constraint and measure progress towards its 2026 goal of enrolling 50% applicants.

##  Project Overview

This project analyzes applicant and enrollment data for Pwani Teknowgalz an organization focused on empowering young women through STEM and digital skills programs.

The project was developed to help the organization understand applicant reach, program popularity, enrollment patterns, and applicant drop-off points. The analysis was transformed into an interactive Power BI dashboard designed to support data-driven decision-making and make the insights accessible to non-technical staff.

##  Project Objectives

The main objectives of this project were to:

- Analyze applicant demographics and application patterns.
- Identify the counties with the highest and lowest applicant reach.
- Determine the most popular programs.
- Analyze applicant distribution by education level.
- Analyze enrollment across counties, programs, and education levels.
- Calculate the overall enrollment rate.
- Identify major applicant drop-off reasons.
- Track the applicant journey from application to enrollment.
- Identify areas where the organization can improve recruitment and enrollment.
- Provide a maintainable dashboard that can be used by non-technical staff.


##  Dataset

The project uses applicant, application, program, county, cohort, and enrollment data stored in a relational database.

The main tables used for the analysis include:

- Applicants – applicant demographic and education information.
- Applications – application status and drop-off information.
- Programs – available Pwani Teknowgalz programs.
- Counties – applicant county information.
- Enrollments – records of successfully enrolled applicants.

The data was intentionally prepared with common data-quality issues before the cleaning process, allowing the project to demonstrate a complete data analytics workflow.

##  Data Cleaning

The applicant and application datasets were cleaned separately before being consolidated for analysis.

The cleaning process included:

- Handling missing values.
- Standardizing text values.
- Removing leading and trailing whitespace.
- Standardizing gender and education-level entries.
- Checking for duplicate records.
- Validating categorical values.
- Standardizing date fields.
- Checking data consistency.
- Saving cleaned datasets for further analysis.

The cleaned datasets were then loaded into the database and combined using SQL.


##  Database & SQL

The project uses SQLite for data storage and SQL for combining and querying the cleaned datasets.

The final analytical dataset combines information from:

- Applicants
- Applications
- Programs
- Counties

This allowed applicant characteristics and application information to be analyzed together while maintaining the structure of the original relational database.

## Exploratory Data Analysis

The analysis was performed using Python and Jupyter Notebook.

### Applicant Analysis

The analysis explored:

- Applicants by county
- Applicants by program
- Applicants by education level
- Applicant age distribution
- Application status

### Enrollment Analysis

Enrollment was analyzed by:

- County
- Program
- Education level
- Overall enrollment rate

### Drop-off Analysis

The project also analyzed why applicants did not progress through the application process.

Key drop-off reasons included:

- Incomplete applications
- Not meeting requirements
- Unable to reach applicant
- Gender mismatch
- Interview capacity limitations


##  Dashboard

The final analysis was visualized using Microsoft Power BI.

The dashboard includes:

### KPI Cards

- Total Applicants
- Total Enrolled
- Enrollment Rate
- Total Drop-outs
- Target Reach
- Current Reach

### Applicant Analysis

- Applicants by County
- Applicants by Program
- Applicants by Education Level

### Enrollment Analysis

- Enrollment by County
- Enrollment by Program
- Enrollment by Education Level

### Applicant Journey

An applicant funnel showing progression through:

Applied → Qualified → Interviewed → Enrolled

### Drop-off Analysis

A visualization of the major reasons applicants fail to progress through the recruitment process.

### Recommendations

The dashboard provides recommendations based on the observed patterns in the data.

##  2026 Target

The dashboard uses a 50% target enrollment goal to provide a clear benchmark for monitoring progress.

The Current Reach indicator allows users to see progress toward this target while filters can be used to explore specific years, counties, programs and education levels.

##  Key Insights

Some of the major findings from the analysis include:

- Mombasa accounts for a large proportion of applicants, while some counties have considerably lower reach.
- Certain programs attract more applicants than others.
- KCSE-level applicants make up the highest proportion of the applicant population.
- Younger applicants represent a larger portion of applications.
- A Good number of applicants do not progress from application to enrollment.
- Incomplete applications are among the important causes of applicant drop-off.
- Recruitment and enrollment capacity can be improved by addressing major drop-off points and underserved areas.

##  Recommendations

Based on the analysis, several actions can help improve enrollment:

- Introduce reminders for applicants who have incomplete applications.
- Clearly communicate eligibility requirements before and during application.
- Provide alternative communication channels for applicants who cannot be reached.
- Increase interview capacity where interview slots are limiting enrollment.
- Strengthen outreach campaigns in counties with low applicant reach(Tana River).
- Increase capacity for highly popular programs(Africa Code Week).
- Continue monitoring enrollment and drop-off patterns through the dashboard.

##  Tools & Technologies

### Programming & Analysis

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

### Database

- SQLite
- SQL

### Visualization

- Microsoft Power BI

### Development Tools

- Visual Studio Code
- Github
