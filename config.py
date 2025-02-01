import os

# Paths
RAW_DATA_PATH = os.path.join("data", "raw", "raw_customer_behavior.csv")
CLEANED_DATA_PATH = os.path.join("data", "cleaned", "cleaned_customer_behavior.csv")

# PostgreSQL Configuration
DB_CONFIG = {
    "dbname": "ecommerce_db",
    "user": "postgres",
    "password": "admin",
    "host": "localhost",
    "port": "5432"
}