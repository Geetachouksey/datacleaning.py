# datacleaning.py
data cleaning and preprocessing
# Netflix Movies and TV Shows — Data Cleaning & Preprocessing

## 🧾 Objective
Clean and preprocess a raw dataset from Kaggle to prepare it for analysis or modeling.

## 📂 Dataset
- **Source:** [Netflix Movies and TV Shows Dataset](https://www.kaggle.com/datasets/shivamb/netflix-shows)
- **Records:** ~8807 rows
- **Features:** show_id, type, title, director, cast, country, date_added, release_year, rating, duration, listed_in, description

## 🧹 Cleaning Steps
1. **Handled Missing Values:**
   - Filled missing `country` with "Unknown".
   - Filled missing `date_added` with mode.
   - Dropped rows with missing `director`.

2. **Removed Duplicates:**
   - Used `drop_duplicates()` to ensure unique entries.

3. **Standardized Text:**
   - Title-cased country/type values.
   - Uppercased rating values.

4. **Formatted Dates:**
   - Converted `date_added` to `dd-mm-yyyy`.

5. **Renamed Columns:**
   - Lowercase and underscores (e.g., `release_year`, `date_added`).

6. **Fixed Data Types:**
   - Converted `release_year` to integer.
   - Converted `date_added` to datetime.

## ✅ Output
- Cleaned dataset: `data/netflix_cleaned.csv`
- Rows after cleaning: ~7780

## ⚙️ How to Run
```bash
pip install -r requirements.txt
python scripts/clean_netflix_data.py

pandas

---

## 📦 4. `requirements.txt`

---

## 💡 Ready-to-Upload GitHub Repo
You can now:
1. Download the Netflix dataset CSV from Kaggle → save as `data/netflix_raw.csv`.
2. Copy the above files into a folder named `netflix-data-cleaning`.
3. Initialize Git & push to GitHub:
   ```bash
   git init
   git add .
   git commit -m "Netflix dataset cleaning project"
   git branch -M main
   git remote add origin https://github.com/yourusername/netflix-data-cleaning.git
   git push -u origin main

