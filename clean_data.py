import pandas as pd
import re
from config import RAW_DATA_PATH, CLEANED_DATA_PATH

def clean_text(text):
    """Clean text fields by removing unwanted symbols."""
    if pd.isna(text):
        return text
    return re.sub(r'[_,;/\|{}[\]!@#%^&*()=+]', '', str(text))

def clean_data():
    # Load raw data
    df = pd.read_csv(RAW_DATA_PATH)

    # First cleaning pass
    df["Comment"] = df["Comment"].apply(clean_text)
    df["Location"] = df["Location"].apply(clean_text)
    df["Purchase Date"] = pd.to_datetime(df["Purchase Date"]).dt.strftime("%Y-%m-%d")

    # Second cleaning pass
    df["Product Category"] = df["Product Category"].str.lower()
    df["Media Access"] = df["Media Access"].str.replace("X", "Twitter")  # Standardize platform names

    # Save cleaned data
    df.to_csv(CLEANED_DATA_PATH, index=False)
    print(f"Cleaned data saved to {CLEANED_DATA_PATH}")

if __name__ == "__main__":
    clean_data()