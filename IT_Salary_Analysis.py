# Import necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import probplot, f_oneway

# Define position categories
position_categories = {
    "IT and Development": [
        "Backend Developer", "Cloud Architect", "Cloud Engineer", "Data Engineer", "Full-Stack Developer",
        "Frontend Developer", "Game Developer", "iOS Developer", "IT Consultant", "IT Manager", "Mobile Developer",
        "Software Architect", "Software Developer in Test", "Software Engineer", "Support Engineer",
        "System Administrator", "Tech Lead", "XR Developer"
    ],
    "Data and Analytics": [
        "Analytics Engineer", "BI Analyst", "BI Consultant", "Big Data Engineer", "Data Analyst", "Data Architect",
        "Data Science Manager", "Data Scientist", "Database Developer (DBA)", "DataOps Team Lead",
        "Machine Learning Engineer", "ML Engineer", "NLP Engineer", "Reporting Engineer", "Senior Data Engineer",
        "Solutions Architect"
    ],
    "Project and Product Management": [
        "Agile Coach", "Application Consultant", "Business Analyst", "ERP Consultant", "Product Analyst",
        "Product Management Praktikant", "Product Manager", "Program Manager", "Project Manager", "Scrum Master",
        "Technical Project Manager"
    ],
    "Sales and Marketing": [
        "Account Manager", "Business Development Manager Operations", "Marketing Analyst", "Presales Engineer",
        "Sales", "Sales Engineer", "Software Sales"
    ],
    "Research and Innovation": [
        "AI Management", "Chief Research Officer", "Computational Linguist", "Computer Vision Researcher",
        "Embedded Developer", "Embedded Software Engineer", "Firmware Engineer", "Head of AI", "Head of Engineering",
        "Head of IT", "Localization", "Localization Producer", "Researcher", "Researcher/Consumer Insights Analyst",
        "Robotics Engineer", "RPA Developer"
    ],
    "Management and Leadership": [
        "CTO", "CTO (CEO, CFO)", "Director of Engineering", "Engineering Manager", "Engineering Team Lead", "Head of BI",
        "IT Operations Manager", "QA Lead", "QA Manager", "Recruiter", "Senior Program Manager", "Senior Scrum Master (RTE)",
        "Solution Architect", "SRE", "Staff Engineer", "Team Lead", "Team Manager", "Tech Leader", "Technical Account Manager",
        "Technical Business Analyst", "Technical Lead", "Test Manager", "UX Researcher", "VP Engineering", "Working Student (QA)"
    ]
}

# Load the dataset
df = pd.read_csv('IT_Salary.csv')

# Clean column names
df.columns = df.columns.str.strip()

# Categorize positions
df['Position Category'] = df['Position'].apply(lambda x: next((k for k, v in position_categories.items() if x in v), 'Other'))

# Calculate average yearly salary for each position category
df_grouped = df.groupby('Position Category')['Yearly salary'].mean().reset_index()
df_grouped = df_grouped.rename(columns={'Yearly salary': 'Average Yearly Salary'})

# Display the grouped data
print(df_grouped.head())

# Select salary and age columns
salary_data = df['Yearly salary']
age_data = df['Age']

# Plot histograms for salary and age
fig, axs = plt.subplots(ncols=2, figsize=(10, 5))
sns.histplot(data=salary_data, kde=True, ax=axs[0])
axs[0].set_title('Salary Histogram')
sns.histplot(data=age_data, kde=True, ax=axs[1])
axs[1].set_title('Age Histogram')
plt.show()

# Calculate sample means
salary_sample_means = np.random.choice(salary_data, (100, 100)).mean(axis=1)
age_sample_means = np.random.choice(age_data, (100, 100)).mean(axis=1)

# Plot histograms for sample means
fig, axs = plt.subplots(ncols=2, figsize=(10, 5))
sns.histplot(salary_sample_means, kde=True, ax=axs[0])
axs[0].set_title('Salary Sample Means Histogram')
sns.histplot(age_sample_means, kde=True, ax=axs[1])
axs[1].set_title('Age Sample Means Histogram')
plt.show()

# Calculate standard error of the mean
salary_sem = np.std(salary_data) / np.sqrt(100)
age_sem = np.std(age_data) / np.sqrt(100)

# Calculate 95% confidence intervals
salary_ci = (np.mean(salary_data) - 1.96 * salary_sem, np.mean(salary_data) + 1.96 * salary_sem)
age_ci = (np.mean(age_data) - 1.96 * age_sem, np.mean(age_data) + 1.96 * age_sem)

# Create Q-Q plots for sample means
probplot(salary_sample_means, dist='norm', plot=plt)
plt.title('Salary Sample Means Q-Q Plot')
plt.show()

probplot(age_sample_means, dist='norm', plot=plt)
plt.title('Age Sample Means Q-Q Plot')
plt.show()

# Print statistics
print('Salary mean:', np.mean(salary_data))
print('Salary standard deviation:', np.std(salary_data))
print('Salary standard error of the mean:', salary_sem)
print('Salary 95% confidence interval:', salary_ci)

print('Age mean:', np.mean(age_data))
print('Age standard deviation:', np.std(age_data))
print('Age standard error of the mean:', age_sem)
print('Age 95% confidence interval:', age_ci)

# Perform one-way ANOVA for yearly salary by main language at work
df = pd.read_csv('IT_Salary.csv')
df = df.dropna(subset=['Yearly salary', 'Main language at work'])
grouped = df.groupby('Main language at work')
means = grouped['Yearly salary'].mean()
stds = grouped['Yearly salary'].std()

f_stat, p_val = f_oneway(df[df['Main language at work'] == 'English']['Yearly salary'],
                         df[df['Main language at work'] == 'German']['Yearly salary'],
                         df[df['Main language at work'] == 'Russian']['Yearly salary'])

# Print ANOVA results
print('One-way ANOVA')
print('-------------')
print(f'F-statistic: {f_stat:.2f}')
print(f'p-value: {p_val:.2f}')
if p_val < 0.05:
    print('Conclusion: Reject the null hypothesis - there is a significant difference in the average yearly salary between IT professionals who work with different main languages.')
else:
    print('Conclusion: Fail to reject the null hypothesis - there is no significant difference in the average yearly salary between IT professionals who work with different main languages.')

# Plot mean yearly salary by main language at work
plt.bar(means.index, means.values)
plt.errorbar(means.index, means.values, yerr=stds.values, fmt='none', ecolor='black', capsize=5)
plt.xlabel('Main Language')
plt.ylabel('Mean Yearly Salary')
plt.title('Mean Yearly Salary by Main Language at Work')
plt.xticks(rotation=45)
plt.figure(figsize=(10, 6))
plt.show()