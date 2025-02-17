from step4_data_analysis_feature_engineering import save_transformed_data

# Debug print to check if execution reaches this point
print("Starting feature engineering...")

# File paths
input_csv = r"C:\Users\shepherd.runesu\Desktop\Projects\Bank-Customer-Attrition-analysis\data\Bank_Customer_Attrition_Insights_Data.csv"
output_csv = r"C:\Users\shepherd.runesu\Desktop\Projects\Bank-Customer-Attrition-analysis\data\bank_customer_transformed.csv"

# Run feature engineering
save_transformed_data(input_csv, output_csv)

# Debug print to check if function call returns
print("Feature engineering function executed.")

# Final print statement
print("Feature engineering completed. Transformed data saved to:", output_csv)

