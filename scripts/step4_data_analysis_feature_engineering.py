import pandas as pd
import os

def create_feature_categories(df):
    """
    Creates new categorical features based on Age, Tenure, and Balance.

    Parameters:
    df (pd.DataFrame): Original DataFrame

    Returns:
    pd.DataFrame: DataFrame with new categorical columns
    """
    
    # Age Categories
    bins_age = [0, 25, 45, 65, 100]
    labels_age = ['Young', 'Middle_Aged', 'Senior', 'Very_Senior']
    df['Age_Category'] = pd.cut(df['Age'], bins=bins_age, labels=labels_age)

    # Tenure Categories
    bins_tenure = [0, 2, 5, 10]
    labels_tenure = ['New_Customer', 'Mid_Term', 'Long_Term']
    df['Tenure_Category'] = pd.cut(df['Tenure'], bins=bins_tenure, labels=labels_tenure)

    # Balance Categories
    bins_balance = [-1, 0, 50000, 100000, 200000, df['Balance'].max()]
    labels_balance = ['Zero_Balance', 'Low_Balance', 'Medium_Balance', 'High_Balance', 'Very_High_Balance']
    df['Balance_Category'] = pd.cut(df['Balance'], bins=bins_balance, labels=labels_balance)

    # Estimated Salary Categories
    bins_salary = [0, 50000, 100000, 150000, df['EstimatedSalary'].max()]
    labels_salary = ['Low_Salary', 'Medium_Salary', 'High_Salary', 'Very_High_Salary']
    df['EstimatedSalary_Category'] = pd.cut(df['EstimatedSalary'], bins=bins_salary, labels=labels_salary)

    return df

def save_transformed_data(input_csv, output_csv):
    """
    Loads data, applies feature engineering, and saves the transformed data.

    Parameters:
    input_csv (str): Path to the original CSV file
    output_csv (str): Path to save the new transformed CSV file
    """
    
    # Load Data
    df = pd.read_csv(input_csv)
    
    # Apply Feature Engineering
    df_transformed = create_feature_categories(df)

    # Ensure the data folder exists
    os.makedirs(os.path.dirname(output_csv), exist_ok=True)

    # Save Transformed Data
    df_transformed.to_csv(output_csv, index=False)
    print(f"Transformed data saved to {output_csv}")
