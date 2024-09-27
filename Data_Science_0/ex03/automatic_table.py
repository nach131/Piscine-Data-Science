import os
import pandas as pd
from tqdm import tqdm
from sqlalchemy import create_engine

db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_user = os.getenv('DB_USER')
db_pass = os.getenv('DB_PASS')
db_name = os.getenv('DB_NAME')

folder = './customer'

connection = f'postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'
engine = create_engine(connection)

# Listar todos los archivos CSV
files = [f for f in os.listdir(folder) if f.endswith('csv')]

# print(files)

for filename in tqdm(files, desc="Importing CSV file", unit="file"):
    table_name = os.path.splitext(filename)[0]
    file_path = os.path.join(folder, filename)

    df = pd.read_csv(file_path)

    if not df.empty:
        df.iloc[:, 0] = pd.to_datetime(
            df.iloc[:, 0], format="%Y-%m-%d %H:%M:%S %Z", utc=True, errors='coerce')

        # Verificar si la conversión fue exitosa
        if df.iloc[:, 0].isnull().any():
            print(f"Warning: Some dates in the first column of {
                  filename} could not be converted. They will be NaT.")

    df.to_sql(table_name, engine, if_exists='replace', index=False)

    print(f"The data has been successfully imported into the table {
          table_name}")

print(f"The files have been imported: \n{files}")
