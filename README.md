# 📊 GitHub Machine Learning Trends Analytics (ETL Pipeline)

An End-to-End Data Engineering and Analytics project that extracts, cleans, stores, and visualizes data about the most popular open-source Machine Learning repositories on GitHub.

## 🛠 Tech Stack
* **Extract:** Python (`requests`), GitHub REST API, API Pagination handling.
* **Transform:** Python (`pandas`), handling nested JSON structures, datetime formatting, data cleaning.
* **Load:** PostgreSQL, `SQLAlchemy`, `psycopg2` (loading the cleaned DataFrame into a relational database).
* **Data Visualization (BI):** Interactive dashboard built in Tableau Public.

## 📈 Result (Dashboard)
**[👉 Click here to view the interactive dashboard on Tableau Public](https://public.tableau.com/app/profile/nurdaulet.abu/viz/GitHubMLTrendsDashboard/Dashboard1)**

## 📂 Project Structure
* `src/extract.py` — Extracts raw JSON data from the GitHub API.
* `src/transform.py` — Cleans and transforms the data using Pandas.
* `src/load.py` — Loads the processed data into a local PostgreSQL database.
* `src/export.py` — Reverse ETL: exports the final data from the database to a CSV file for Tableau.

## 🚀 How to Run Locally
1. Clone the repository.
2. Install the required dependencies: 
```bash
   pip install -r requirements.txt
