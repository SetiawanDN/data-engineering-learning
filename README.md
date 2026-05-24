# Mini ETL Pipeline Project

This project demonstrates a simple ETL (Extract, Transform, Load) pipeline using Python, Pandas, and SQLite.

## Features
- Read CSV data
- Filter data
- Detect duplicate records
- Clean duplicate data
- Handle missing values
- Transform data
- Export cleaned CSV
- Load data into SQLite database
- Execute SQL queries using Python

## Technologies Used
- Python
- Pandas
- SQLite

## Project Structure

data-engineering-learning/
│
├── employees.csv
├── clean_employees.csv
├── company.db
│
└── scripts/
    ├── step1_read_csv.py
    ├── step2_filter.py
    ├── step3_duplicate_check.py
    ├── step4_export_clean.py
    ├── step5_sqlite_load.py
    ├── step6_transform.py
    └── step7_validation.py

## How to Run

Run Python scripts using:

```bash
py script_name.py