import sys
import pandas as pd
import subprocess 

if len(sys.argv) < 2:
    print("Please provide dataset path")
    sys.exit(1)

file_path = sys.argv[1]

data = pd.read_csv(file_path, header=1)
data.to_csv("data_raw.csv", index=False)

print("Data saved as data_raw.csv")


print("Starting Preprocessing...")
subprocess.run(['python', 'preprocess.py', 'data_raw.csv'])