import pandas as pd

# read parquet file
df = pd.read_parquet(r'C:\Users\Zawar Khan\Downloads\yellow_tripdata_2024-01.parquet')

# change parquet file to csv 
df.to_csv('yellow_2023_01.csv', index = False)