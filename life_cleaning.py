import pandas as pd

# Load raw dataset
df = pd.read_csv("LifeData.csv")

# Remove unwanted column
df = df.drop(columns=["Unnamed: 22"], errors='ignore')

# Strip leading/trailing spaces in column names
df.columns = df.columns.str.strip()

# Handle missing values (basic fill or drop based on strategy)
# For now, drop rows with missing Life expectancy (target)
df = df.dropna(subset=["Life expectancy"])

# Option: Fill other missing values with column mean (for numeric columns only)
numeric_cols = df.select_dtypes(include=["float64", "int64"]).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

# Confirm changes
print("✅ Cleaned shape:", df.shape)
print("🔍 Missing values remaining:\n", df.isnull().sum())
df.to_csv("Life_cleaned.csv", index=False)
