import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file
df = pd.read_csv("/Users/ridhaaahmed/Documents/employee_performance_dataset.csv")

# Preview first 5 rows
print("First 5 rows:")
print(df.head())

# Check dataset info
print("\nDataset info:")
print(df.info())

# Convert numeric columns
df["Attendance_Rate"] = pd.to_numeric(df["Attendance_Rate"], errors='coerce')
df["Performance_Score"] = pd.to_numeric(df["Performance_Score"], errors='coerce')

# Drop rows with missing values
df = df.dropna(subset=["Attendance_Rate", "Performance_Score"])

# Check first few rows after conversion
print("\nAfter numeric conversion:")
print(df[["Attendance_Rate", "Performance_Score"]].head())

# Calculate correlation
correlation = df["Attendance_Rate"].corr(df["Performance_Score"])
print(f"\nCorrelation between Attendance Rate and Performance Score: {correlation:.2f}")

# Scatter plot with trendline
plt.figure(figsize=(8,6))
sns.regplot(x="Attendance_Rate", y="Performance_Score", data=df)
plt.title("Attendance Rate vs Performance Score")
plt.xlabel("Attendance Rate")
plt.ylabel("Performance Score")
plt.show()
