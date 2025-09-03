# Data Analyst Portfolio – Ridhaa Ahmed

## Overview
This portfolio showcases my data analysis skills using a real-world employee performance dataset. The dataset contains information about employees' attendance, performance scores, projects completed, salary, and other key attributes. The goal of this analysis was to explore the relationship between attendance rate and performance score, and gain insights useful for management decisions.

## Dataset Description
- **Employee_ID**: Unique identifier for each employee  
- **Name**: Employee’s full name  
- **Department**: Department in which the employee works  
- **Hire_Date**: Date the employee was hired  
- **Salary**: Employee’s salary  
- **Attendance_Rate**: Fraction of days the employee attended work  
- **Projects_Completed**: Number of projects completed by the employee  
- **Performance_Score**: Performance evaluation score  
- **Manager**: Name of the employee’s manager  

The dataset was cleaned and transformed to ensure numeric fields were correctly formatted, and missing values were handled appropriately.

## Analysis Steps
1. Loaded the dataset in Python using `pandas`.
2. Renamed columns for clarity.
3. Converted `Attendance_Rate` and `Performance_Score` to numeric values.
4. Removed rows with missing values in these columns.
5. Created a scatter plot with a regression line using `seaborn` to visualize the relationship between attendance and performance.

### Key Code Snippets
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV
df = pd.read_csv("employee_performance_dataset.csv", header=0)

# Rename columns
df.columns = ["Employee_ID", "Name", "Department", "Hire_Date", 
              "Salary", "Attendance_Rate", "Projects_Completed", 
              "Performance_Score", "Manager"]

# Convert to numeric
df['Attendance_Rate'] = pd.to_numeric(df['Attendance_Rate'], errors='coerce')
df['Performance_Score'] = pd.to_numeric(df['Performance_Score'], errors='coerce')

# Drop missing values
df = df.dropna(subset=['Attendance_Rate', 'Performance_Score'])

# Scatter plot with regression line
plt.figure(figsize=(8,6))
sns.regplot(x="Attendance_Rate", y="Performance_Score", data=df)
plt.title("Attendance Rate vs Performance Score")
plt.xlabel("Attendance Rate")
plt.ylabel("Performance Score")
plt.show()

## Insights
- Higher attendance generally correlates with higher performance scores.
- Some employees with lower attendance still perform well, suggesting other factors affect performance.
- These insights can assist management in making data-driven decisions about productivity and resource allocation.

## Skills Demonstrated
- Python (Pandas, Matplotlib, Seaborn)
- Data Cleaning and Transformation
- Exploratory Data Analysis (EDA)
- Visualization and Reporting

## Contact
- GitHub: [Ridhaa9A](https://github.com/Ridhaa9A)
- Email: ridhaaahmed2002@gmail.com

## Analysis Result

![Attendance vs Performance](https://github.com/Ridhaa9A/data-analyst-portfolio/blob/main/3.Visualizations%20%E2%80%93%20charts%2C%20scatter%20plots%2C%20histograms%2C%20etc/Attendance%20Rate%20vs%20Peformance%20Score%3AScatter%20graph%20.png)
