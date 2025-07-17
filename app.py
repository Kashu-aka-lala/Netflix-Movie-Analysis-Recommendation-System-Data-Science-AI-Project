import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create outputs folder if it doesn't exist
output_dir = 'outputs'
os.makedirs(output_dir, exist_ok=True)

# Load dataset
df = pd.read_csv("Netflix_data.csv")

# Convert Release_Date to datetime
df['Release_Date'] = pd.to_datetime(df['Release_Date'], errors='coerce')

# Create Release_Year column
df['Release_Year'] = df['Release_Date'].dt.year

# -----------------------------
# Q1: Distribution of Movies vs TV Shows
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='Type', palette='Set2')
plt.title('Distribution of Content Type on Netflix')
plt.xlabel('Type')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig(f"{output_dir}/content_type_distribution.png")
plt.close()

# Save Q1 values
df['Type'].value_counts().to_csv(f"{output_dir}/content_type_counts.csv")

# -----------------------------
# Q2: Top 10 countries contributing content (clean and enhanced version)
# Q2: Top 10 countries contributing content – Vertical bar version
top_countries = df['Country'].value_counts().head(10)

plt.figure(figsize=(10, 6))
sns.set(style="whitegrid")
sns.barplot(x=top_countries.index, y=top_countries.values, palette='viridis')
plt.title('Top 10 Content Producing Countries on Netflix', fontsize=14)
plt.xlabel('Country', fontsize=12)
plt.ylabel('Number of Titles', fontsize=12)
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.tight_layout()
plt.savefig(f"{output_dir}/top_10_countries.png", dpi=300)
plt.close()

# Save Q2 values
top_countries.to_csv(f"{output_dir}/top_10_countries.csv")

# -----------------------------
# Q3: Most common maturity ratings
rating_counts = df['Rating'].value_counts().head(10)

plt.figure(figsize=(8, 5))
sns.barplot(x=rating_counts.values, y=rating_counts.index, palette='pastel')
plt.title('Top 10 Most Common Maturity Ratings on Netflix')
plt.xlabel('Number of Titles')
plt.ylabel('Rating')
plt.tight_layout()
plt.savefig(f"{output_dir}/top_10_maturity_ratings.png")
plt.close()

# Save Q3 values
rating_counts.to_csv(f"{output_dir}/top_10_maturity_ratings.csv")

# -----------------------------
# Q4: Trend of Netflix content released over the years
yearly_counts = df['Release_Year'].value_counts().sort_index()

plt.figure(figsize=(12, 6))
yearly_counts.plot(kind='line', marker='o', color='green')
plt.title('Trend of Netflix Content Released Over the Years')
plt.xlabel('Release Year')
plt.ylabel('Number of Titles')
plt.grid(True)
plt.tight_layout()
plt.savefig(f"{output_dir}/content_trend_by_year.png")
plt.close()

# Save Q4 values
yearly_counts.to_csv(f"{output_dir}/content_trend_by_year.csv")

print("✅ All plots and value files saved in 'outputs/' folder.")
# -----------------------------
