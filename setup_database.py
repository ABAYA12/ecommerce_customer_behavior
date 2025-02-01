import psycopg2
import pandas as pd
from config import DB_CONFIG, CLEANED_DATA_PATH

def setup_database():
    # Connect to PostgreSQL
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()

    # Create table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customer_behavior (
            customer_id VARCHAR(20) PRIMARY KEY,
            customer_name TEXT,
            customer_age INT,
            gender TEXT,
            purchase_date DATE,
            product_category TEXT,
            product_price FLOAT,
            quantity INT,
            total_purchase_amount FLOAT,
            payment_method TEXT,
            location TEXT,
            media_access TEXT,
            returns INT,
            churn INT,
            comment TEXT
        )
    """)

    # Insert data with explicit column mapping
    df = pd.read_csv(CLEANED_DATA_PATH)
    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO customer_behavior (
                customer_id, customer_name, customer_age, gender, 
                purchase_date, product_category, product_price, quantity, 
                total_purchase_amount, payment_method, location, media_access, 
                returns, churn, comment
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            row["Customer ID"], row["Customer Name"], row["Customer Age"], row["Gender"],
            row["Purchase Date"], row["Product Category"], row["Product Price"], row["Quantity"],
            row["Total Purchase Amount"], row["Payment Method"], row["Location"], row["Media Access"],
            row["Returns"], row["Churn"], row["Comment"]
        ))

    conn.commit()
    cursor.close()
    conn.close()
    print("Data uploaded to PostgreSQL")

if __name__ == "__main__":
    setup_database()