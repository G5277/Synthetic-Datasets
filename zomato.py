import pandas as pd
import random
from faker import Faker

fake = Faker()

# List of sample data
restaurant_names = ["The Royal Bistro", "Spice Paradise", "Green Bowl", "Taste of India", "Urban Grill", "Flavors of China", "Pizza Plaza", "Sushi World", "Café Mocha", "Taco Fiesta"]
cuisines = ["Italian", "Chinese", "Indian", "Mexican", "American", "Japanese", "French", "Mediterranean", "Thai", "Greek"]
locations = ["New York", "Los Angeles", "Chicago", "San Francisco", "Houston", "Boston", "Dallas", "Washington", "Miami", "Seattle"]
price_ranges = ["$", "$$", "$$$", "$$$$"]
ratings = [1, 2, 3, 4, 5]
types_of_meals = ["Lunch", "Dinner", "Brunch", "Breakfast"]
delivery_options = ["Yes", "No"]

data = []
for _ in range(300):
    restaurant = {
        "Restaurant Name": random.choice(restaurant_names),
        "Cuisine": random.choice(cuisines),
        "Location": random.choice(locations),
        "Rating": random.choice(ratings),
        "Price Range": random.choice(price_ranges),
        "Delivery Available": random.choice(delivery_options),
        "Meals Available": random.choice(types_of_meals),
        "Address": fake.address(),
        "Contact": fake.phone_number()
    }
    data.append(restaurant)

df = pd.DataFrame(data)

df.to_csv("Data/zomato_dataset.csv", index=False)

print(df.head())