from generate_data import generate_synthetic_data
from clean_data import clean_data
from setup_database import setup_database

def main():
    print("Step 1: Generating synthetic data...")
    generate_synthetic_data()

    print("\nStep 2: Cleaning data...")
    clean_data()

    print("\nStep 3: Setting up database...")
    setup_database()

    print("\nWorkflow completed!")

if __name__ == "__main__":
    main()