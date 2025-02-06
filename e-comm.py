import pandas as pd
import random

def random_product_name(category):
    product_names = {
        'Electronics': ['Wireless Mouse', 'Bluetooth Speaker', 'Smartphone', 'Laptop', 'Smartwatch', 'Headphones', 'Tablet'],
        'Clothing': ['T-Shirt', 'Jacket', 'Sweater', 'Jeans', 'Shoes', 'Dress', 'Pants'],
        'Home Appliances': ['Refrigerator', 'Washing Machine', 'Microwave', 'Air Conditioner', 'Vacuum Cleaner', 'Dishwasher'],
        'Furniture': ['Sofa', 'Dining Table', 'Chair', 'Bookshelf', 'Cabinet', 'Couch'],
        'Beauty': ['Lipstick', 'Foundation', 'Skincare Cream', 'Shampoo', 'Perfume', 'Nail Polish'],
        'Sports': ['Football', 'Basketball', 'Yoga Mat', 'Bicycle', 'Tennis Racket', 'Soccer Ball']
    }
    
    return random.choice(product_names[category])

def random_category():
    categories = {
        'Electronics': ['Mobile Phones', 'Laptops', 'Tablets', 'Smartwatches', 'Headphones', 'Speakers'],
        'Clothing': ['T-Shirts', 'Jackets', 'Sweaters', 'Shoes', 'Pants', 'Dresses'],
        'Home Appliances': ['Microwave', 'Washing Machine', 'Air Conditioner', 'Refrigerator', 'Vacuum Cleaner'],
        'Furniture': ['Sofa', 'Table', 'Chair', 'Bookshelf', 'Cabinet'],
        'Beauty': ['Makeup', 'Skin Care', 'Hair Care', 'Fragrance', 'Nail Polish'],
        'Sports': ['Football', 'Basketball', 'Tennis Racket', 'Yoga Mat', 'Bicycle']
    }
    category = random.choice(list(categories.keys()))
    sub_category = random.choice(categories[category])
    return category, sub_category

def generate_price(category):
    if category == 'Electronics':
        return round(random.uniform(50, 1500), 2)
    elif category == 'Clothing':
        return round(random.uniform(10, 200), 2)
    elif category == 'Home Appliances':
        return round(random.uniform(50, 1000), 2)
    elif category == 'Furniture':
        return round(random.uniform(100, 1500), 2)
    elif category == 'Beauty':
        return round(random.uniform(5, 200), 2)
    elif category == 'Sports':
        return round(random.uniform(15, 800), 2)

def random_customer_age():
    return random.randint(18, 65)

def random_customer_gender():
    return random.choice(['Male', 'Female'])

def generate_purchase_history(age, category):
    if age < 30:
        return random.randint(5, 50)
    elif 30 <= age < 50:
        return random.randint(10, 30)
    else:
        return random.randint(0, 20)

def generate_review_sentiment(price):
    if price < 50:
        return random.choice(['Neutral', 'Negative'])
    elif 50 <= price < 200:
        return random.choice(['Neutral', 'Positive'])
    else:
        return random.choice(['Positive', 'Very Positive'])

def generate_review_rating(price):
    if price < 50:
        return random.randint(1, 3)
    elif 50 <= price < 200:
        return random.randint(3, 5)
    else:
        return random.randint(4, 5)

data = []
for i in range(8000):
    product_id = f"P{i+1:04d}"
    category, sub_category = random_category()
    product_name = random_product_name(category)  
    price = generate_price(category)
    customer_age = random_customer_age()
    customer_gender = random_customer_gender()
    purchase_history = generate_purchase_history(customer_age, category)
    review_rating = generate_review_rating(price)
    review_sentiment = generate_review_sentiment(price)
    
    data.append([product_id, product_name, category, sub_category, price, customer_age, customer_gender, purchase_history, review_rating, review_sentiment])

df = pd.DataFrame(data, columns=[
    'Product_ID', 'Product_Name', 'Category', 'Sub_Category', 'Price', 'Customer_Age', 
    'Customer_Gender', 'Purchase_History', 'Review_Rating', 'Review_Sentiment'
])

df.to_csv('./Data/refined_ecommerce_product_data.csv', index=False)

print("Refined synthetic dataset saved as 'refined_ecommerce_product_data.csv' with 8000 unique records.")
