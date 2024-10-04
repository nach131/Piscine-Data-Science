import os
import pandas as pd
from sqlalchemy import create_engine

db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_user = os.getenv('DB_USER')
db_pass = os.getenv('DB_PASS')
db_name = os.getenv('DB_NAME')

folder = '../subject/customer/'

connection = f'postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'
engine = create_engine(connection)

# Listar todos los archivos CSV
files = [f for f in os.listdir(folder) if f.endswith('csv')]

for filename in files:
    table_name = os.path.splitext(filename)[0]
    file_path = os.path.join(folder, filename)

    # Leer el archivo CSV por chunks
    chunk_size = 10000
    count = 1

    print(f"\nImported: {filename}")

    try:
        for chunk in pd.read_csv(file_path, chunksize=chunk_size):

            if not chunk.empty:
                chunk.iloc[:, 0] = pd.to_datetime(
                    chunk.iloc[:, 0], format="%Y-%m-%d %H:%M:%S %Z", utc=True, errors='coerce')

                # Verificar si la conversión fue exitosa
                if chunk.iloc[:, 0].isnull().any():
                    print(f"Warning: Some dates in the first column of {
                        filename} could not be converted. They will be NaT.")

                chunk.to_sql(table_name, engine,
                             if_exists='append', index=False)
            count += 1
            print(f"Chunck: {count}", end='\r', flush=True)

    except pd.errors.EmptyDataError:
        print(f"Warning: The file {filename} is empty.")
    except Exception as e:
        print(f"Error processing file {filename}: {e}")

# print(f"The files have been imported: \n{files}")
