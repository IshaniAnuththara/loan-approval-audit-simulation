# loan-approval-audit-simulation
Loan Approval Audit Simulation  is a  data analysis project built after learning NumPy and Pandas.  The goal was to simulate a basic audit process for an AI-based loan approval system using synthetic data.
Project Overview

In this project, I:
Generated 1,000 synthetic loan applications using NumPy
Created features such as:

Credit Score
Income
Loan Amount
AI Approval Probability

Simulated:
Data poisoning (impossible credit scores)
Approval bias (lower probabilities for low-income group)

Detected:
Outliers in credit scores
Disparities in approval probability between income groups
Exported flagged records into a CSV report

Tools Used
Python
NumPy
Pandas

What This Project Demonstrates:
Data generation with NumPy
Data manipulation and filtering with Pandas
Group-based statistical comparison
Basic anomaly detection using logical conditions
Exporting structured audit results

Notes:
This is a simulated dataset created for learning purposes.
The bias and data corruption were intentionally introduced to practice detection techniques.
Output

The script generates:
Console-based audit report
audit_red_flags.csv containing flagged records
