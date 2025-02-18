import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

base_file = r"C:\Users\shepherd.runesu\Desktop\Projects\Bank-Customer-Attrition-analysis"

def load_data(file_path):
    """Load the transformed dataset."""
    return pd.read_csv(file_path)

def save_plot(fig, filename):
    """Save a plot as an image file inside the 'results\figures' folder."""
    os.makedirs(os.path.dirname(base_file), exist_ok=True)
    fig.savefig(rf"{base_file}\results\figures\{filename}", bbox_inches='tight')
    plt.close(fig)

def plot_churn_distribution(df):
    """Plot and save the overall churn distribution."""
    fig, ax = plt.subplots(figsize=(6,4))
    sns.countplot(x='Exited', hue='Exited', data=df, palette=['blue', 'red'], ax=ax, legend=False)
    ax.set_xticks([0, 1]) 
    ax.set_xticklabels(['Stayed', 'Churned'])
    ax.set_title("Customer Churn Distribution")
    ax.set_xlabel("Churn")
    ax.set_ylabel("Count")
    
    save_plot(fig, "churn_distribution.png")

def plot_churn_by_category(df, category_col):
    """Plot and save churn rates across different categories."""
    fig, ax = plt.subplots(figsize=(8,5))
    sns.barplot(x=category_col, y='Exited', hue=category_col, data=df, 
            estimator=lambda x: sum(x)/len(x)*100, 
            errorbar=None, palette='coolwarm', ax=ax, legend=False)

    ax.set_title(f"Churn Rate by {category_col}")
    ax.set_ylabel("Churn Rate (%)")
    ax.set_xlabel(category_col)
    plt.xticks(rotation=45)

    save_plot(fig, f"churn_by_{category_col}.png")

def run_visualization(input_csv):
    """Runs data visualization and saves plots as images."""
    df = load_data(input_csv)

    # Save churn distribution plot
    plot_churn_distribution(df)

    # Save churn by key categories
    plot_churn_by_category(df, 'Age_Category')
    plot_churn_by_category(df, 'Balance_Category')
    plot_churn_by_category(df, 'IsActiveMember')

    print(f"Results visualizations saved in '{base_file}/figures' directory.")
  
