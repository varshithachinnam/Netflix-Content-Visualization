import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
url = "https://raw.githubusercontent.com/mushfiq98/Netflix-Dataset-Visualization/main/netflix_titles.csv"
df = pd.read_csv(url)
print("--- NETFLIX DATASET SAMPLE ---")
print(df.head(3))
df["country"] = df["country"].fillna("Unknown")
df["cast"] = df["cast"].fillna("No Cast")
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sns.countplot(x="type", data=df, palette="Set2")
plt.title("Content Type on Netflix (Movies vs TV Shows)")
plt.subplot(1, 2, 2)
top_countries = df["country"].value_counts().head(5)
top_countries.plot(kind="bar", color="skyblue")
plt.title("Top 5 Countries with Most Content")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("netflix_report.png")
print(
    "\nAnalysis complete! Visualizations saved successfully as 'netflix_report.png'."
)