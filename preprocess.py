import sys
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
import subprocess

def main():
    # --- Load data with multi-level header ---
    input_path = sys.argv[1] if len(sys.argv) > 1 else '2024-2025 La Liga Players Stats.csv'
    df = pd.read_csv(input_path, header=[0,1])

    # --- Flatten multi-level columns ---
    df.columns = [' '.join([str(c) for c in col if str(c) != '']).strip() for col in df.columns.values]

    print("Columns after flattening:")
    print(df.columns.tolist())

    # --- Find player column ---
    possible_player_cols = [c for c in df.columns if 'player' in c.lower()]
    if not possible_player_cols:
        print("⚠️ Could not find any column with 'player' in its name!")
        return
    player_col = possible_player_cols[0]
    print(f"✅ Using player column: '{player_col}'")

    # --- Drop repeated header row if exists ---
    if all(df.iloc[0].astype(str) == df.columns.astype(str)):
        df = df[1:].copy()

    # --- Drop unnecessary columns if exist ---
    if 'Matches' in df.columns:
        df = df.drop(columns=['Matches'])

    # --- Detect numeric columns automatically ---
    exclude_cols = [player_col, 'Nation', 'Pos', 'Squad']
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    numeric_cols = [c for c in numeric_cols if c not in exclude_cols]

    # Convert numeric columns to numeric and fill NaN
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    df[numeric_cols] = df[numeric_cols].fillna(0)

    df = df.drop_duplicates()

    # --- Feature transformation ---
    for col in ['Pos', 'Squad']:
        if col in df.columns:
            le = LabelEncoder()
            df[col+'_encoded'] = le.fit_transform(df[col].astype(str))

    # --- StandardScaler for numeric features ---
    scaler = StandardScaler()
    scale_features = [c for c in ['Gls', 'Ast', 'xG', 'xAG', 'PrgP'] if c in df.columns]
    for col in scale_features:
        if df[col].std() != 0:  # Avoid scaling constant columns
            df[col] = scaler.fit_transform(df[[col]])

    # --- Select important columns if exist ---
    selected_cols = [player_col, 'Squad', 'Age', 'Gls', 'Ast', 'xG', 'xAG', 'PrgP', 'Pos_encoded', 'Squad_encoded']
    selected_cols = [c for c in selected_cols if c in df.columns]
    df = df[selected_cols]

    # --- Age discretization ---
    if 'Age' in df.columns:
        bins = [0, 23, 30, 100]
        labels = ['Young', 'Prime', 'Veteran']
        df['AgeGroup'] = pd.cut(df['Age'], bins=bins, labels=labels, include_lowest=True)

    # --- Save preprocessed data ---
    df.to_csv('data_preprocessed.csv', index=False)
    print("✅ Preprocessed data saved to data_preprocessed.csv")

    # --- Optionally run analytics ---
    try:
        subprocess.run(['python', 'analytics.py', 'data_preprocessed.csv'], check=True)
    except FileNotFoundError:
        print("⚠️ analytics.py not found, skipping analytics step.")

if __name__ == "__main__":
    main()