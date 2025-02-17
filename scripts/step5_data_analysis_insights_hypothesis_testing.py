import pandas as pd
import scipy.stats as stats
import os

def load_data(file_path):
    """Load the transformed CSV file into a DataFrame."""
    return pd.read_csv(file_path)

def analyze_churn_by_category(df, category_col):
    """Analyze churn rate within different categories of a given column."""
    churn_summary = df.groupby(category_col)['Exited'].value_counts(normalize=True).unstack()
    churn_summary.columns = ['Stayed', 'Churned']
    return churn_summary * 100  # Convert to percentage

def perform_chi_square_test(df, column):
    """Perform a Chi-Square test to determine if a categorical feature impacts churn."""
    contingency_table = pd.crosstab(df[column], df['Exited'])
    chi2, p_value, _, _ = stats.chi2_contingency(contingency_table)
    return p_value

def run_analysis(input_csv, output_file):
    """Runs data analysis and hypothesis testing, saving results to a file."""
    df = load_data(input_csv)

    # Ensure the data folder exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # Open file to write analysis results
    with open(output_file, "w") as f:
        f.write("=== Customer Churn Data Analysis ===\n\n")

        # Churn Analysis
        churn_by_age = analyze_churn_by_category(df, 'Age_Category')
        churn_by_balance = analyze_churn_by_category(df, 'Balance_Category')
        churn_by_active_status = analyze_churn_by_category(df, 'IsActiveMember')

        f.write("Churn by Age Category:\n")
        f.write(churn_by_age.to_string() + "\n\n")
        
        f.write("Churn by Balance Category:\n")
        f.write(churn_by_balance.to_string() + "\n\n")

        f.write("Churn by Active Member Status:\n")
        f.write(churn_by_active_status.to_string() + "\n\n")

        # Hypothesis Testing
        p_value_age = perform_chi_square_test(df, 'Age_Category')
        p_value_balance = perform_chi_square_test(df, 'Balance_Category')
        p_value_active = perform_chi_square_test(df, 'IsActiveMember')

        f.write("=== Hypothesis Testing Results ===\n")
        f.write(f"Chi-Square Test for Age and Churn: p-value = {p_value_age:.4f}\n")
        f.write(f"Chi-Square Test for Balance and Churn: p-value = {p_value_balance:.4f}\n")
        f.write(f"Chi-Square Test for Active Status and Churn: p-value = {p_value_active:.4f}\n\n")

        # Conclusion
        f.write("=== Conclusions ===\n")
        if p_value_age < 0.05:
            f.write("Age has a statistically significant impact on churn.\n")
        if p_value_balance < 0.05:
            f.write("Balance has a statistically significant impact on churn.\n")
        if p_value_active < 0.05:
            f.write("Active status has a statistically significant impact on churn.\n")

    print(f"Analysis results saved to {output_file}")
