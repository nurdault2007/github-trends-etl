import pandas as pd
from sqlalchemy import create_engine
import os

def export_to_csv():
    engine = create_engine('postgresql://username:password@localhost:5432/dbname')
    query = "SELECT * FROM trending_repos ORDER BY stars DESC;"
    df = pd.read_sql(query, con=engine)
    output_dir = "data/processed"
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "tableau_export.csv")
    df.to_csv(output_file, index=False, encoding='utf-8')
    print(f"File is ready for Tableau: {output_file}")

if __name__ == "__main__":
    export_to_csv()
