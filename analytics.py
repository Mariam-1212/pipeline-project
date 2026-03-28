import sys
import pandas as pd
import subprocess

def main():
    input_path = sys.argv[1] if len(sys.argv) > 1 else 'data_preprocessed.csv'
    df = pd.read_csv(input_path)
    
    

    df['Impact'] = df['Gls'] + df['Ast']
    top_players = df.sort_values(by='Impact', ascending=False).head(5)['Player'].tolist()
    with open('insight1.txt', 'w') as f:
        f.write("Top 5 Impactful Players (Scaled Gls + Ast): " + ", ".join(top_players))
        
        
    top_squad = df.groupby('Squad')['xG'].mean().idxmax()
    with open('insight2.txt', 'w') as f:
        f.write(f"Squad with highest average scaled xG: {top_squad}")
        
    age_counts = df['AgeGroup'].value_counts().to_string()
    with open('insight3.txt', 'w') as f:
        f.write("Player distribution by age group:\n" + age_counts)
    
    print("Analytics insights saved.")
    subprocess.run(['python', 'visualize.py', 'data_preprocessed.csv'])

if __name__ == "__main__":
    main()