import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("Life_cleaned.csv")

# Set default style
sns.set(style="whitegrid")

# -------------------------------
# 1. Distribution of Life Expectancy
plt.figure(figsize=(8, 5))
sns.histplot(df['Life expectancy'], bins=30, kde=True, color='skyblue')
plt.title('Distribution of Life Expectancy')
plt.xlabel('Life Expectancy (Years)')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

# -------------------------------
# 2. Correlation Heatmap (Only numeric columns)
plt.figure(figsize=(12, 10))
corr = df.select_dtypes(include='number').corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.show()

# -------------------------------
# 3. Top 10 Countries by Avg Life Expectancy
top_countries = df.groupby('country')['Life expectancy'].mean().sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 5))
sns.barplot(x=top_countries.values, y=top_countries.index, palette='viridis')
plt.title('Top 10 Countries by Average Life Expectancy')
plt.xlabel('Average Life Expectancy')
plt.tight_layout()
plt.show()

# -------------------------------
# 4. Life Expectancy Over Time by Status
plt.figure(figsize=(10, 5))
sns.lineplot(data=df, x='Year', y='Life expectancy', hue='Status', estimator='mean')
plt.title('Life Expectancy Over Time by Status')
plt.ylabel('Average Life Expectancy')
plt.tight_layout()
plt.show()

# -------------------------------
# 5. Life Expectancy vs GDP
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='GDP', y='Life expectancy', hue='Status')
plt.title('Life Expectancy vs GDP')
plt.xlabel('GDP')
plt.ylabel('Life Expectancy')
plt.tight_layout()
plt.show()

# -------------------------------
# 6. Life Expectancy vs Schooling
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='Schooling', y='Life expectancy', hue='Status')
plt.title('Life Expectancy vs Schooling')
plt.xlabel('Years of Schooling')
plt.ylabel('Life Expectancy')
plt.tight_layout()
plt.show()
