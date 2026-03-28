import sys
import pandas as pd
from sklearn.cluster import KMeans

def main():
    input_path = sys.argv[1] if len(sys.argv) > 1 else 'data_preprocessed.csv'
    df = pd.read_csv(input_path)

    features = ['Gls', 'Ast', 'xG', 'xAG']
    kmeans = KMeans(n_clusters=3, random_state=42, n_init='auto')
    df['Cluster'] = kmeans.fit_predict(df[features])
    
    cluster_counts = df['Cluster'].value_counts().sort_index().to_string()
    with open('clusters.txt', 'w') as f:
        f.write("Samples per cluster:\n" + cluster_counts)
        
    print("Clustering completed and results saved.")

if __name__ == "__main__":
    main()