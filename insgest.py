import sys
import pandas as pd

if len(sys.argv) < 2:
    print("Please provide dataset path")
    sys.exit(1)

file_path = sys.argv[1]

# Load dataset
data = pd.read_csv(file_path)

# Save a copy as data_raw.csv
data.to_csv("data_raw.csv", index=False)

print("Data saved as data_raw.csv")