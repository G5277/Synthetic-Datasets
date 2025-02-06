import pandas as pd
import random

# Job positions
job_positions = ["Software Developer", "Data Scientist", "Product Manager", "UX Designer", "Web Developer", "Data Analyst", "HR Manager"]

# Sample skills
skills_list = [
    "Python", "Java", "C++", "SQL", "Machine Learning", "Deep Learning", "Data Science", 
    "JavaScript", "HTML", "CSS", "React", "Angular", "Cloud Computing", "AWS", "Docker", 
    "Project Management", "Agile", "Git", "Excel", "Power BI", "Tableau", "Communication"
]

# Education levels
education_levels = ["Bachelor's", "Master's", "PhD", "Associate's"]

# Application statuses
statuses = ["Interview", "Rejected", "Offer Made", "Under Review", "Not Shortlisted"]

# Locations
locations = ["New York", "San Francisco", "Los Angeles", "Chicago", "Boston", "Seattle", "Austin", "Dallas"]

# Function to generate synthetic job application data
def generate_synthetic_job_data(num_samples=8000):
    data = []
    
    for _ in range(num_samples):
        applicant_id = random.randint(1000, 9999)
        applicant_name = f"Applicant_{applicant_id}"
        job_position = random.choice(job_positions)
        experience = random.randint(0, 10)  # Experience in years
        skills = random.sample(skills_list, random.randint(3, 7))  # Randomly select 3-7 skills
        education = random.choice(education_levels)
        application_status = random.choice(statuses)
        location = random.choice(locations)
        expected_salary = random.randint(50000, 150000)  # Expected salary in USD
        resume_score = random.randint(50, 100)  # Resume match score out of 100
        
        # Create the data entry
        data.append([
            applicant_id, applicant_name, job_position, experience, ", ".join(skills), education,
            application_status, location, expected_salary, resume_score
        ])
    
    return pd.DataFrame(data, columns=["Applicant ID", "Applicant Name", "Job Position", "Experience (Years)", 
                                       "Skills", "Education Level", "Application Status", "Location", 
                                       "Expected Salary", "Resume Score"])

# Generate dataset and save it to CSV
df = generate_synthetic_job_data(8000)
df.to_csv("./Data/synthetic_job_application_dataset.csv", index=False)

print("Synthetic Job Application Dataset created with 8000 samples: synthetic_job_application_dataset.csv")
