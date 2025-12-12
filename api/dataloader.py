import polars as pl
import sqlite3
import os

db_file = "my_database.db"

csv_files = {
    "vehicles.csv": "vehicles",
    "drivers.csv": "drivers",
    "scenarios.csv": "scenarios",
    "other.csv": "other_table"
}

conn = sqlite3.connect(db_file)
cursor = conn.cursor()

for csv_file, table_name in csv_files.items():
    cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}';")
    table_exists = cursor.fetchone() is not None
    
    row_count = 0
    if table_exists:
        cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
        row_count = cursor.fetchone()[0]
        
    if row_count == 0:
        print(f"Loading {csv_file} into {table_name}...")
        df = pl.read_csv(csv_file)
        
        columns = ", ".join(f"{col} TEXT" for col in df.columns)
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})")
        
        placeholders = ", ".join("?" for _ in df.columns)
        cursor.executemany(
            f"INSERT INTO {table_name} VALUES ({placeholders})",
            df.to_numpy().tolist()    
        )
        
        conn.commit()
    else:
        print(f"Skipping {table_name}, already has data.")

conn.close()
print("Done!")