import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Create Sample Dataset
# -----------------------------
data = {
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'Math': [78, 66, 44, 88, 55, 95],
    'Science': [80, 89, 92, 85, 90, 98],
    'English': [66, 42, 85, 90, 56, 96]
}

df = pd.DataFrame(data)

# -----------------------------
# Add Total Column
# -----------------------------
df['Total'] = df['Math'] + df['Science'] + df['English']

# -----------------------------
# Display Dataset
# -----------------------------
print("\n===== DATASET PREVIEW =====")
print(df)

# -----------------------------
# Average Marks (Only Numeric Columns)
# -----------------------------
print("\n===== AVERAGE MARKS =====")
print(df.mean(numeric_only=True))

# -----------------------------
# Summary Statistics
# -----------------------------
print("\n===== SUMMARY STATISTICS =====")
print(df.describe())

# -----------------------------
# VISUALIZATION SECTION
# -----------------------------

# 1️⃣ Bar Chart - Subject Average
plt.figure()
df[['Math', 'Science', 'English']].mean().plot(kind='bar')
plt.title("Average Marks per Subject")
plt.ylabel("Average Marks")
plt.xlabel("Subjects")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# 2️⃣ Gender-wise Total Score
plt.figure()
sns.barplot(x='Gender', y='Total', data=df)
plt.title("Total Score by Gender")
plt.tight_layout()
plt.show()

# 3️⃣ Correlation Heatmap (Only Numeric)
plt.figure()
sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

print("\n✅ Project Executed Successfully!")
