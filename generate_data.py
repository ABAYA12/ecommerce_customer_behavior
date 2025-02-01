import pandas as pd
from faker import Faker
import numpy as np
from datetime import datetime, timedelta
from config import RAW_DATA_PATH
from product_comments import product_comments  # Import product-specific comments

# Initialize Faker and seed for reproducibility
fake = Faker()
np.random.seed(42)
Faker.seed(42)

# Ghana-specific locations
ghana_locations = [
    "Accra", "Kumasi", "Tamale", "Sekondi-Takoradi", "Ashaiman",
    "Cape Coast", "Obuasi", "Tema", "Madina", "Wa", "Ho", "Koforidua"
]

# Media access platforms
media_access_platforms = ["Facebook", "X", "LinkedIn", "WhatsApp", "TikTok", "Instagram"]

# Product categories
product_categories = [
    "Electronics", "Fashion", "Home & Kitchen", "Groceries",
    "Beauty", "Books", "Sports", "Toys"
]

# Payment methods
payment_methods = ["Credit Card", "Mobile Money", "PayPal", "Cash on Delivery"]

def generate_synthetic_data(num_records=10_000):
    """Generate synthetic e-commerce data."""
    data = {
        "Customer ID": [f"CUST-{i:06d}" for i in range(1, num_records + 1)],
        "Customer Name": [fake.name() for _ in range(num_records)],
        "Customer Age": np.random.randint(18, 70, size=num_records),
        "Gender": np.random.choice(["Male", "Female", "Other"], size=num_records),
        "Purchase Date": [fake.date_between(start_date="-2y", end_date="today") for _ in range(num_records)],
        "Product Category": np.random.choice(product_categories, size=num_records),
        "Product Price": np.round(np.random.uniform(10, 500, size=num_records), 2),
        "Quantity": np.random.randint(1, 10, size=num_records)
    }
    
    # Calculate total purchase amount
    data["Total Purchase Amount"] = np.round(data["Product Price"] * data["Quantity"], 2)
    data["Payment Method"] = np.random.choice(payment_methods, size=num_records)
    data["Location"] = np.random.choice(ghana_locations, size=num_records)
    data["Media Access"] = np.random.choice(media_access_platforms, size=num_records)
    data["Returns"] = np.random.choice([0, 1], size=num_records, p=[0.85, 0.15])
    data["Churn"] = np.random.choice([0, 1], size=num_records, p=[0.7, 0.3])
    
    # Generate comments related to product category
    comments = []
    for category in data["Product Category"]:
        if np.random.rand() < 0.5:  # 50% chance of having a comment
            comment = np.random.choice(product_comments.get(category, [np.nan]))
        else:
            comment = np.nan
        comments.append(comment)
    
    data["Comment"] = comments
    
    df = pd.DataFrame(data)
    df.to_csv(RAW_DATA_PATH, index=False)
    print(f"Synthetic data generated and saved to {RAW_DATA_PATH}")

if __name__ == "__main__":
    generate_synthetic_data()