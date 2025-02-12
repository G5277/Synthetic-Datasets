import random
import pandas as pd

# Define possible symptoms, conditions, severity, duration, treatments, and age groups
symptoms = ['Fever', 'Cough', 'Headache', 'Shortness of breath', 'Runny Nose', 'Fatigue', 'Sore Throat', 'Body Ache', 'Nausea', 'Vomiting']
conditions = {
    'Fever': ['Flu', 'COVID-19', 'Malaria'],
    'Cough': ['Cold', 'Flu', 'COVID-19', 'Bronchitis'],
    'Headache': ['Migraine', 'Stress', 'Sinusitis', 'COVID-19'],
    'Shortness of breath': ['COVID-19', 'Pneumonia', 'Asthma'],
    'Runny Nose': ['Cold', 'Allergies'],
    'Fatigue': ['Anemia', 'COVID-19', 'Chronic Fatigue Syndrome'],
    'Sore Throat': ['Cold', 'Tonsillitis', 'COVID-19'],
    'Body Ache': ['Flu', 'COVID-19', 'Chronic Fatigue Syndrome'],
    'Nausea': ['Food Poisoning', 'Flu', 'Migraine'],
    'Vomiting': ['Food Poisoning', 'Gastroenteritis']
}

severity_levels = ['Mild', 'Moderate', 'Severe']
durations = {
    'Mild': ['1 day', '2 days'],
    'Moderate': ['2-3 days', '1 week'],
    'Severe': ['1 week', 'Several weeks']
}

treatments = {
    'Flu': 'Rest, Hydration, Pain relievers',
    'COVID-19': 'Oxygen therapy, Rest, Hydration',
    'Cold': 'Rest, Hydration, Decongestants',
    'Anemia': 'Iron supplements, Rest',
    'Food Poisoning': 'Hydration, Anti-nausea medications',
    'Migraine': 'Pain relievers, Rest, Hydration'
}

age_groups = {
    'Fever': ['Adults', 'Elderly'],
    'Cough': ['Children', 'Adults'],
    'Headache': ['Adults', 'Elderly'],
    'Shortness of breath': ['Adults', 'Elderly'],
    'Runny Nose': ['Children', 'Adults'],
    'Fatigue': ['Adults', 'Elderly'],
    'Sore Throat': ['Children', 'Adults'],
    'Body Ache': ['Adults', 'Elderly'],
    'Nausea': ['Adults'],
    'Vomiting': ['Adults', 'Children']
}

regions = ['Global', 'Seasonal', 'Tropical', 'Cold climates']

# Function to generate synthetic health data
def generate_health_data(num_entries=300):
    data = []
    
    for _ in range(num_entries):
        symptom = random.choice(symptoms)
        condition = random.choice(conditions[symptom])
        severity = random.choice(severity_levels)
        duration = random.choice(durations[severity])
        treatment = treatments.get(condition, 'Rest, Hydration')
        age_group = random.choice(age_groups[symptom])
        region = random.choice(regions)
        
        data.append({
            'Symptom': symptom,
            'Condition': condition,
            'Severity': severity,
            'Duration': duration,
            'Possible Causes': 'Viral infection, Bacterial infection, Stress',  # Random possible causes for simplicity
            'Treatment': treatment,
            'Age Group': age_group,
            'Region': region
        })
    
    return pd.DataFrame(data)

# Generate the synthetic dataset
df = generate_health_data(300)

# Save to CSV
df.to_csv('Data/synthetic_health_symptoms_data.csv', index=False)

# Show first few rows
print(df.head())
