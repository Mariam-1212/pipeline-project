import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import subprocess

def main():
    input_path = sys.argv[1] if len(sys.argv) > 1 else 'data_preprocessed.csv'
    df = pd.read_csv(input_path)
    
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
  
    sns.histplot(df['Age'], bins=15, kde=True, ax=axes[0])
    axes[0].set_title('Age Distribution')
   
    corr = df[['Gls', 'Ast', 'xG', 'xAG', 'PrgP']].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=axes[1])
    axes[1].set_title('Feature Correlation')
  
    sns.scatterplot(data=df, x='xG', y='Gls', hue='AgeGroup', ax=axes[2])
    axes[2].set_title('Goals (Gls) vs Expected Goals (xG)')
    
    plt.tight_layout()
    plt.savefig('summary_plot.png')
    print("Summary plot saved.")
    subprocess.run(['python', 'cluster.py', 'data_preprocessed.csv'])

if __name__ == "__main__":
    main()