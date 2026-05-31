import pandas as pd
from sqlalchemy import create_engine
import os

def load_data_to_postgres(csv_file):
    print("Reading cleaned files...")
    if not os.path.exists(csv_file):
         print(f"Error file not found!")
         return
         
    df = pd.read_csv(csv_file)
    
    print("Connecting to PostgreSQL...")
    engine = create_engine('postgresql://etl_user:12345@localhost:5432/github_etl')
    
    print("Uploading data to db...")
    df.to_sql(name='trending_repos', con=engine, if_exists='replace', index=False)
    
    print(f"Success! {len(df)} lines loaded into 'trending_repos' in db 'github_etl'.")

if __name__ == "__main__":
    processed_file = "data/processed/cleaned_github_data.csv"
    load_data_to_postgres(processed_file)
