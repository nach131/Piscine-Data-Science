import os
import pandas as pd
from sqlalchemy import create_engine

db_user = 'nmota-bu'
db_pass = 'mysecretpassword'
db_host = 'db'
db_port = '5432'
db_name = 'piscineds'

folder = './customer'

connection = f'postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'
engine = create_engine(connection)

# Listar todos los archivos CSV

for filename in os.listdir(folder):
    if filename.endswith('.csv'):
        table_name = os.path.splitext(filename)[0]

        file_path = os.path.join(folder, filename)
        # print(file_path)
        df = pd.read_csv(file_path)

        df.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f"Los datos se han importado correctamente en la tabla {
          table_name}")

print("Se han importado todos los ficheros")
