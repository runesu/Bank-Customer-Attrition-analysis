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

import matplotlib.pyplot as plt
import seaborn as sns

import matplotlib.pyplot as plt
import seaborn as sns

def plot_churn_distribution(df):
    """Plot and save the overall churn distribution."""
    fig, ax = plt.subplots(figsize=(6, 4))

    # Create the count plot
    bars = sns.countplot(x='Exited', hue='Exited', data=df, palette=['blue', 'red'], ax=ax, legend=False)

    # Add labels inside each bar
    for bar in bars.containers:
        ax.bar_label(bar, fmt="%d", padding=-20, color='white', weight='bold', fontsize=12)  

    # Add grid lines
    ax.yaxis.grid(True, linestyle='dashed', alpha=0.6)  # Dashed horizontal grid lines
    ax.set_axisbelow(True)  # Ensures grid lines stay behind bars

    # Formatting the x-axis
    ax.set_xticks([0, 1]) 
    ax.set_xticklabels(['Stayed', 'Churned'])

    # Titles and labels
    ax.set_title("Customer Churn Distribution")
    ax.set_xlabel("Churn")
    ax.set_ylabel("Count")

    # Save the plot
    save_plot(fig, "churn_distribution.png")



def plot_churn_by_category(df, category_col):
    """Plot and save churn rates across different categories."""
    fig, ax = plt.subplots(figsize=(8, 5))
    
    # Create the bar plot
    bars = sns.barplot(x=category_col, y='Exited', hue=category_col, data=df, 
                       estimator=lambda x: sum(x)/len(x)*100, 
                       errorbar=None, palette='coolwarm', ax=ax, legend=False)

    # Annotate bars with percentage values
    for bar in bars.containers:
        ax.bar_label(bar, fmt="%.1f%%", padding=3)

    ax.set_title(f"Churn Rate by {category_col}")
    ax.set_ylabel("Churn Rate (%)")
    ax.set_xlabel(category_col)
    ax.set_ylim(0, 100)  # Ensure y-axis ranges from 0 to 100%
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
  
