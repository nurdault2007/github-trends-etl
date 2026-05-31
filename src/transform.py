import pandas as pd
import json
import os

def clean_github_data(input_file, output_file):
    print("get unprocessed data...")
    with open(input_file, 'r', encoding='utf-8') as f:
        raw_data = json.load(f)

    cleaned_data = []
    for item in raw_data:
        cleaned_data.append({
            'repo_id': item.get('id'),
            'name': item.get('name'),
            'owner': item.get('owner', {}).get('login'), 
            'html_url': item.get('html_url'),
            'language': item.get('language'), 
            'stars': item.get('stargazers_count', 0),
            'forks': item.get('forks_count', 0),
            'created_at': item.get('created_at'),
            'updated_at': item.get('updated_at'),
            'has_issues': item.get('has_issues', False)
        })

    df = pd.DataFrame(cleaned_data)
    print("Clean data...")
    df['language'] = df['language'].fillna('Unknown')
    df['created_at'] = pd.to_datetime(df['created_at'])
    df['updated_at'] = pd.to_datetime(df['updated_at'])
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    df.to_csv(output_file, index=False, encoding='utf-8')
    
    print(f"\nReady! Cleaned {len(df)} totally.")
    print(f"Data saved in: {output_file}\n")

    print(df[['name', 'language', 'stars']].head(5))
    
    return df

if __name__ == "__main__":
    input_path = "data/raw/raw_github_data.json"
    output_path = "data/processed/cleaned_github_data.csv"
    
    if os.path.exists(input_path):
        clean_github_data(input_path, output_path)
    else:
        print(f"Error file not found")
