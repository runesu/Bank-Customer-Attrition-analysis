from step4_data_analysis_feature_engineering import save_transformed_data
from step5_data_analysis_insights_hypothesis_testing import run_analysis
from step6_data_visualization import run_visualization

##########################STEP 4: FEATURE ENGINEERING#########################

# File paths
input_csv = r"C:\Users\shepherd.runesu\Desktop\Projects\Bank-Customer-Attrition-analysis\data\Bank_Customer_Attrition_Insights_Data.csv"
output_csv = r"C:\Users\shepherd.runesu\Desktop\Projects\Bank-Customer-Attrition-analysis\data\bank_customer_transformed.csv"

# Run feature engineering
save_transformed_data(input_csv, output_csv)


##########################STEP 5: DATA ANALYSIS INSIGHTS AND HYPOTHESIS TESTING#########################

# File path to transformed data file
input_csv_transformed = output_csv
output_file = r"C:\Users\shepherd.runesu\Desktop\Projects\Bank-Customer-Attrition-analysis\results\data_analysis_results.txt"

# Run analysis
run_analysis(input_csv_transformed, output_file)


#########################STEP 6: DATA VISUALIZATION#########################

# Run visualization
run_visualization(input_csv_transformed)
