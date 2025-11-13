import pandas as pd

# Load dataset
df = pd.read_csv('data/netflix_raw.csv')

# ----- Basic Inspection -----
print("Initial Shape:", df.shape)
print("Missing values:\n", df.isnull().sum())

# ----- Handle Missing Values -----
# Fill missing 'country' with 'Unknown'
df['country'] = df['country'].fillna('Unknown')

# Fill missing 'date_added' with mode
df['date_added'] = df['date_added'].fillna(df['date_added'].mode()[0])

# Drop rows with missing 'director' (optional)
df = df.dropna(subset=['director'])

# ----- Remove Duplicates -----
df = df.drop_duplicates()

# ----- Standardize Text Columns -----
df['type'] = df['type'].str.strip().str.title()             # e.g., 'Movie' or 'Tv Show'
df['country'] = df['country'].str.strip().str.title()
df['rating'] = df['rating'].str.strip().str.upper()

# ----- Fix Date Format -----
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce').dt.strftime('%d-%m-%Y')

# ----- Clean Column Names -----
df.columns = (
    df.columns.str.strip()
              .str.lower()
              .str.replace(' ', '_')
)

# ----- Check Data Types -----
df['release_year'] = df['release_year'].astype(int)

# ----- Save Cleaned Dataset -----
df.to_csv('data/netflix_cleaned.csv', index=False)

print("\n✅ Cleaning complete! Cleaned data saved to 'data/netflix_cleaned.csv'")
print("Final Shape:", df.shape)
