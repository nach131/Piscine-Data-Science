import os
import pandas as pd
from tqdm import tqdm
from sqlalchemy import create_engine

db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_user = os.getenv('DB_USER')
db_pass = os.getenv('DB_PASS')
db_name = os.getenv('DB_NAME')

folder = '../subject/item/'

files = [
    'item.csv',
]

connection = f'postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'
engine = create_engine(connection)


for filename in files:
    table_name = os.path.splitext(filename)[0]
    file_path = os.path.join(folder, filename)

    # Leer el archivo CSV por chunks
    chunk_size = 10000
    count = 1

    print(f"\nImported: {filename}")

    try:
        for chunk in pd.read_csv(file_path, chunksize=chunk_size):

            # solo los registro que tinen datos
            filtered = chunk.dropna(
                subset=['category_id', 'category_code', 'brand'], how='all')

            filtered.to_sql(table_name, engine,
                            if_exists='append', index=False)
            count += 1
            print(f"Chunck: {count}", end='\r', flush=True)

    except pd.errors.EmptyDataError:
        print(f"Warning: The file {filename} is empty.")
    except Exception as e:
        print(f"Error processing file {filename}: {e}")
