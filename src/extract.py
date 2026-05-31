import os
import time
import json
import requests
from dotenv import load_dotenv
load_dotenv()
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
if not GITHUB_TOKEN:
    raise ValueError("Token not found! Check .env")

BASE_URL = "https://api.github.com/search/repositories"
HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def fetch_github_repos(topic, max_pages=5):

    all_repos = []
    
    print(f"Starting collect data by topic: {topic}...")

    for page in range(1, max_pages + 1):
        params = {
            "q": f"topic:{topic}",
            "sort": "stars",     
            "order": "desc",     
            "per_page": 100,     
            "page": page        
        }
        response = requests.get(BASE_URL, headers=HEADERS, params=params)

        if response.status_code == 200:
            data = response.json()
            items = data.get("items", [])
            all_repos.extend(items)
            
            print(f"Page {page}/{max_pages} succesfully installed ({len(items)} repos).")
        else:
            print(f"Error at page {page}: {response.status_code}")
            print(response.text)
            break 

        time.sleep(2) 

    return all_repos

def save_to_json(data, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"\nData succesfully saved in {filename}. Total: {len(data)}")

if __name__ == "__main__":
    search_topic = "machine-learning"
    raw_data = fetch_github_repos(topic=search_topic, max_pages=3)
    save_to_json(raw_data, "data/raw/raw_github_data.json")
