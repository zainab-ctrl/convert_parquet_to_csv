import pandas as pd

# read parquet file
parquet_file_path = 'C:\Users\Zawar Khan\Downloads\yellow_tripdata_2024-01.parquet'
df = pd.read_parquet(parquet_file_path)

# change parquet file to csv 
name_csv_file = 'yellow_2023_01.csv'
df.to_csv(name_csv_file, index = False)