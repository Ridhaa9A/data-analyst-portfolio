# Ridhaa Ahmed – Data Analyst Portfolio

Welcome to my Data Analyst portfolio! This repository showcases my skills in data cleaning, analysis, and visualization using Python and real-world datasets. It highlights projects I’ve completed to practice and demonstrate my analytical capabilities.

---

## 📂 Project Structure

1. **Dataset Description**  
   Contains details about the datasets used, where they come from, and what each column represents.  

2. **Visualizations**  
   Includes charts, scatter plots, and histograms generated during analysis. Key insights are visualized for easier understanding.  

3. **Code Snippets**  
   Highlights key Python scripts used for cleaning, transforming, and analyzing the data. Full code with comments is provided for clarity.  

4. **Datasets**  
   Original CSV files used for analysis.  

---

## 📊 Sample Project: Employee Performance Analysis

**Objective:**  
Analyze the relationship between employee attendance and performance scores to uncover trends and insights.

**Steps Taken:**  
1. Loaded the CSV dataset using Python and Pandas.  
2. Cleaned the data: renamed columns, converted numeric columns, and removed missing values.  
3. Visualized relationships using scatter plots with regression lines.  
4. Derived insights on how attendance correlates with performance.  

**Key Code Used:**
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("employee_performance_dataset.csv", header=0)

# Rename columns
df.columns = [
    "Employee_ID", "Name", "Department", "Hire_Date", 
    "Salary", "Attendance_Rate", "Projects_Completed", 
    "Performance_Score", "Manager"
]

# Convert to numeric and drop missing values
df['Attendance_Rate'] = pd.to_numeric(df['Attendance_Rate'], errors='coerce')
df['Performance_Score'] = pd.to_numeric(df['Performance_Score'], errors='coerce')
df = df.dropna(subset=['Attendance_Rate', 'Performance_Score'])

# Scatter plot
plt.figure(figsize=(8,6))
sns.regplot(x="Attendance_Rate", y="Performance_Score", data=df)
plt.title("Attendance Rate vs Performance Score")
plt.xlabel("Attendance Rate")
plt.ylabel("Performance Score")
plt.show()
