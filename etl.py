import os
import pandas as pd
from sqlalchemy import create_engine

# Folder paths
base_path = os.path.dirname(os.path.abspath(__file__))
input_folder = os.path.join(base_path, 'input_pdfs')
output_folder = os.path.join(base_path, 'output_data')

# Create output folder if needed
os.makedirs(output_folder, exist_ok=True)

# Look for CSV or Excel file
csv_file = None
excel_file = None

for f in os.listdir(input_folder):
    if f.endswith('.csv'):
        csv_file = os.path.join(input_folder, f)
    elif f.endswith('.xlsx'):
        excel_file = os.path.join(input_folder, f)

if not csv_file and not excel_file:
    print("❌ No CSV or Excel files found in 'input_pdfs' folder.")
    exit()

# Load the file
if csv_file:
    df = pd.read_csv(csv_file)
    print(f"✅ Loaded CSV file: {csv_file}")
elif excel_file:
    df = pd.read_excel(excel_file)
    print(f"✅ Loaded Excel file: {excel_file}")

# Optional: clean or inspect data
print("📊 Preview:")
print(df.head())

# Save to SQLite
db_path = os.path.join(base_path, 'bank_financials.db')
engine = create_engine(f"sqlite:///{db_path}")
df.to_sql("financials", con=engine, if_exists="replace", index=False)

print(f"✅ Data loaded into SQLite → Table: 'financials'")

