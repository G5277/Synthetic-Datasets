import pandas as pd
import random
import itertools

# Expanded Sentiment-related content examples
positive_phrases = [
    "Just got my dream job! Feeling on top of the world!", "Today was amazing! I’m so grateful for everything.",
    "So proud of my progress, everything is falling into place!", "I can't believe how far I've come. So grateful!",
    "Nothing beats the feeling of accomplishing your goals!", "So excited about my new adventure in life!",
    "I just finished reading an amazing book that changed my perspective!", "Life is so beautiful right now!"
]
negative_phrases = [
    "I can't believe how bad today was. Everything went wrong.", "Feeling so down, things aren't going well.",
    "I regret my decision. This was a terrible choice.", "Disappointed with the way things are turning out.",
    "This has been the worst week ever. I need a break!", "No matter what I do, nothing seems to work out.",
    "I can't shake this feeling of failure. I feel stuck.", "Everything is falling apart and I don't know what to do."
]
neutral_phrases = [
    "Just finished a long day at work. Time to relax.", "Here's a picture of my new lunch. #yum", 
    "Started a new project today. Let's see how it goes.", "I just took a walk in the park. Feeling good.",
    "Went to a coffee shop today. The vibe was nice.", "Catch me at the gym later today.", "It's a regular Monday.",
    "Spent the afternoon doing some reading. A pretty chill day."
]

# Random user profiles (followers, bio, age, location)
user_profiles = [
    {"followers": random.randint(100, 1000), "bio": "Just another social media user.", "age": random.randint(18, 35), "location": "New York"},
    {"followers": random.randint(1000, 5000), "bio": "Tech enthusiast, foodie, and travel lover.", "age": random.randint(25, 40), "location": "San Francisco"},
    {"followers": random.randint(5000, 20000), "bio": "Fitness coach, motivator, and influencer.", "age": random.randint(22, 30), "location": "Los Angeles"},
    {"followers": random.randint(20000, 100000), "bio": "Lifestyle guru and content creator.", "age": random.randint(30, 50), "location": "London"},
    {"followers": random.randint(500, 3000), "bio": "Freelance photographer. Love the outdoors.", "age": random.randint(20, 35), "location": "Paris"}
]

# Expanded list of context-dependent hashtags
hashtags = ["#love", "#hate", "#life", "#fitness", "#tech", "#food", "#travel", "#selfcare", "#motivation", "#weekend", "#grateful", "#workout", "#newbeginnings", "#inspiration", "#dreams", "#books", "#blessed", "#adventure", "#lifeisgood", "#positivity"]

def generate_synthetic_social_media_data(num_samples=8000):
    data = []
    
    for _ in range(num_samples):
        # Randomly select post type (positive, negative, or neutral)
        sentiment = random.choice(["positive", "negative", "neutral"])
        
        if sentiment == "positive":
            content = random.choice(positive_phrases)
        elif sentiment == "negative":
            content = random.choice(negative_phrases)
        else:
            content = random.choice(neutral_phrases)
        
        # Randomly assign a user profile
        user_profile = random.choice(user_profiles)
        
        # Randomly select a set of hashtags
        post_hashtags = random.sample(hashtags, random.randint(1, 4))
        
        # Randomly generate engagement values
        likes = random.randint(100, 1000)
        comments = random.randint(0, 200)
        shares = random.randint(0, 50)
        
        # Sentiment-based engagement: positive posts get more engagement
        if sentiment == "positive":
            likes += random.randint(100, 300)
            comments += random.randint(50, 150)
        elif sentiment == "negative":
            likes += random.randint(10, 50)
            comments += random.randint(5, 30)
        
        # Sentiment label (1: positive, 0: negative, 2: neutral)
        label = {"positive": 1, "negative": 0, "neutral": 2}[sentiment]
        
        # Create the data entry
        data.append([
            content, 
            user_profile["followers"], 
            user_profile["bio"], 
            user_profile["age"], 
            user_profile["location"],
            post_hashtags, 
            likes + comments + shares,  # Total engagement
            label
        ])
    
    return pd.DataFrame(data, columns=["Post Content", "Followers", "User Bio", "Age", "Location", "Hashtags", "Engagement", "Sentiment"])

# Generate dataset and save it to CSV
df = generate_synthetic_social_media_data(8000)
df.to_csv("./Data/synthetic_social_media_sentiment_refined.csv", index=False)

print("Refined Synthetic Social Media Sentiment Dataset created with 8000 samples: synthetic_social_media_sentiment_refined.csv")
