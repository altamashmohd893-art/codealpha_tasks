import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Sample Dataset
# -----------------------------
data = {
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'Math': [23, 34, 90, 45, 76, 95],
    'Science': [70, 49, 52, 85, 70, 98],
    'English': [75, 92, 85, 90, 72, 96]
}

df = pd.DataFrame(data)

# Add Total Column
df['Total'] = df['Math'] + df['Science'] + df['English']

# -----------------------------
# 1️⃣ Bar Chart - Average Marks per Subject
# -----------------------------
plt.figure()
df[['Math', 'Science', 'English']].mean().plot(kind='bar')
plt.title("Average Marks per Subject")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# -----------------------------
# 2️⃣ Gender-wise Total Score
# -----------------------------
plt.figure()
sns.barplot(x='Gender', y='Total', data=df)
plt.title("Total Score by Gender")
plt.tight_layout()
plt.show()

# -----------------------------
# 3️⃣ Correlation Heatmap
# -----------------------------
plt.figure()
sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

print("\n✅ Task 3 Visualization Completed Successfully!")
