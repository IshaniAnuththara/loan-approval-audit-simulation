import pandas as pd
import numpy as np

# Create 1000 applications
np.random.seed(42)
n_apps = 1000

data = {
    'Application_ID': np.arange(1, n_apps + 1),
    'Credit_Score': np.random.normal(700, 50, n_apps),
    'Income': np.random.normal(50000, 15000, n_apps),
    'Loan_Amount': np.random.normal(15000, 5000, n_apps),
    'AI_Approval_Prob': np.random.uniform(0, 1, n_apps) # 0 to 1 probability
}

audit_df = pd.DataFrame(data)

# POISONING THE DATA:

audit_df.loc[10:19, 'Credit_Score'] = 9999

# BIAS INJECTION:

audit_df.loc[audit_df['Income'] < 30000, 'AI_Approval_Prob'] *= 0.1

print("Audit Data Generated!")


# --- TASK 1: Detect Data Poisoning ---

poisoned_indices = np.where(audit_df['Credit_Score'] > 850)[0]

print("--- AUDIT REPORT: DATA INTEGRITY ---")
if len(poisoned_indices) > 0:
    print(f"ALERT: {len(poisoned_indices)} poisoned rows detected!")
    # Show the IDs of the suspicious applications
    print(f"Suspicious Application IDs: {audit_df.loc[poisoned_indices, 'Application_ID'].values}")
else:
    print("No data poisoning detected.")

print("\n" + "="*40 + "\n")

# --- TASK 2: Analyze the Bias ---

low_income = audit_df[audit_df['Income'] < 30000]
high_income = audit_df[audit_df['Income'] > 50000]

# Calculate the mean approval probability for both
low_income_avg = low_income['AI_Approval_Prob'].mean()
high_income_avg = high_income['AI_Approval_Prob'].mean()

print("--- AUDIT REPORT: AI BIAS ANALYSIS ---")
print(f"Avg Approval Prob (Low Income < $30k):  {low_income_avg:.4f}")
print(f"Avg Approval Prob (High Income > $50k): {high_income_avg:.4f}")

# Calculate the gap
gap = high_income_avg / low_income_avg
print(f"\nDisparity Ratio: {gap:.2f}x")
print(f"Conclusion: High-income earners are {gap:.2f} times more likely to be approved.")

# 1. Identify Poisoned Rows (Credit Score > 850)
poisoned_indices = np.where(audit_df['Credit_Score'] > 850)[0]
poisoned_rows = audit_df.iloc[poisoned_indices]

# 2. Identify "Bias Victims"

bias_victims = audit_df[(audit_df['Credit_Score'] > 750) & (audit_df['AI_Approval_Prob'] < 0.1)]

# 3. Create the "Red Flag Report"
red_flags = pd.concat([poisoned_rows, bias_victims]).drop_duplicates()

print(f"--- AUDIT COMPLETE ---")
print(f"Impossible Data Points Found: {len(poisoned_rows)}")
print(f"Potential Bias Victims Found: {len(bias_victims)}")

# Export to CSV for the client
red_flags.to_csv('audit_red_flags.csv', index=False)
print("\n'audit_red_flags.csv' has been generated for the CEO.")