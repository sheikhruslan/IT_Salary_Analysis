# IT Salary Analysis

This project analyzes IT salary data to provide insights into salary distributions, position categories, and the impact of different factors on salaries. The analysis is performed using Python and various data science libraries.

## Files

- **IT_Salary_Analysis.py**: The main script that performs the data analysis.
- **IT_Salary.csv**: The dataset containing IT salary information.
- **README.md**: This file.

## Requirements

- Python 3.x
- pandas
- numpy
- seaborn
- matplotlib
- scipy

You can install the required libraries using pip:

```bash
pip install pandas numpy seaborn matplotlib scipy
```

## Usage
Ensure that IT_Salary.csv is in the same directory as IT_Salary_Analysis.py.

Run the script:

```bash
python IT_Salary_Analysis.py
```

## Analysis Performed

Position Categorization: Positions are categorized into different groups such as "IT and Development", "Data and Analytics", etc.

Data Cleaning: Column names are stripped of any leading or trailing whitespace.

Salary Analysis:

Average yearly salary for each position category is calculated and displayed.

Histograms for salary and age distributions are plotted.

Sample means for salary and age are calculated and plotted.

Standard error of the mean and 95% confidence intervals for salary and age are calculated.

Q-Q plots for sample means are created.

ANOVA Analysis: A one-way ANOVA is performed to analyze the impact of the main language at work on yearly salary.
Output

## The script outputs various statistics and plots, including:

Average yearly salary by position category.
Histograms for salary and age distributions.
Histograms for sample means of salary and age.
Q-Q plots for sample means.
Standard error of the mean and 95% confidence intervals for salary and age.
Results of the one-way ANOVA for yearly salary by main language at work.
