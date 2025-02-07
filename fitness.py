import pandas as pd
import random

# New Workout types
workout_types = ["Running", "Weight Training", "Yoga", "Cycling", "Swimming", "HIIT", "Walking", "Pilates", "Crossfit", "Zumba"]

# Expanded Mood List
moods = ["Energized", "Tired", "Motivated", "Unmotivated", "Focused", "Relaxed", "Stressed", "Happy", "Confident", "Bored"]

# Fitness goals and progress tracking
goals = ["Weight Loss", "Muscle Gain", "Maintain Weight", "Increase Flexibility"]
progress_tracking = ["Excellent (90%-100%)", "Good (70%-89%)", "Average (50%-69%)", "Needs Improvement (30%-49%)", "Poor (0%-29%)"]

# Caloric Intake Ranges for different activity levels
activity_levels = {
    "Sedentary": (1800, 2200),
    "Active": (2200, 2800),
    "Very Active": (2800, 3500)
}

# Hydration level categories
hydration_levels = ["Low (<2L)", "Moderate (2L-3L)", "High (>3L)"]

# Function to generate synthetic health and fitness data with enhanced uniqueness
def generate_synthetic_health_data(num_samples=8000):
    data = []
    
    for _ in range(num_samples):
        user_id = random.randint(1000, 9999)
        user_name = f"User_{user_id}"
        age = random.randint(18, 65)
        
        # Assigning Age Groups
        if age <= 25:
            age_group = "18-25 (Young Adults)"
        elif 26 <= age <= 35:
            age_group = "26-35 (Adults)"
        elif 36 <= age <= 45:
            age_group = "36-45 (Mid-Aged Adults)"
        elif 46 <= age <= 55:
            age_group = "46-55 (Older Adults)"
        else:
            age_group = "56+ (Seniors)"
        
        gender = random.choice(["Male", "Female", "Non-binary"])
        height = random.randint(150, 190)  # Height in cm
        weight = random.randint(45, 120)  # Weight in kg
        body_fat_percentage = round(random.uniform(10.0, 40.0), 1)  # Body fat percentage
        
        # Assigning Caloric Intake based on activity level
        activity_level = random.choice(list(activity_levels.keys()))
        caloric_intake = random.randint(*activity_levels[activity_level])
        
        workout_type = random.choice(workout_types)
        workout_duration = random.randint(20, 90)  # Duration of workout in minutes
        weekly_exercise_frequency = random.randint(3, 7)  # Number of workout days per week
        sleep_hours = random.randint(6, 10)  # Average sleep hours
        goal = random.choice(goals)
        progress = random.choice(progress_tracking)  # Fitness progress
        mood = random.choice(moods)  # User's mood during workout
        hydration = random.choice(hydration_levels)  # Hydration levels
        
        # Create the data entry
        data.append([
            user_id, user_name, age_group, age, gender, height, weight, body_fat_percentage, caloric_intake, 
            workout_type, workout_duration, weekly_exercise_frequency, sleep_hours, goal, progress, 
            mood, hydration
        ])
    
    return pd.DataFrame(data, columns=[
        "User ID", "User Name", "Age Group", "Age", "Gender", "Height (cm)", "Weight (kg)", "Body Fat Percentage",
        "Daily Caloric Intake", "Workout Type", "Workout Duration (min)", "Weekly Exercise Frequency", 
        "Sleep Hours", "Goal", "Progress", "Mood", "Hydration"
    ])

# Generate dataset and save it to CSV
df = generate_synthetic_health_data(8000)
df.to_csv("./Data/refined_synthetic_health_fitness_dataset.csv", index=False)

print("Refined Synthetic Health and Fitness Dataset created with 8000 samples: refined_synthetic_health_fitness_dataset.csv")
