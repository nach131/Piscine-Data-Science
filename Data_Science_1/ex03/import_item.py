import pandas as pd
from sqlalchemy import create_engine

db_user = 'nmota-bu'
db_pass = 'mysecretpassword'
db_host = 'db'
db_port = '5432'
db_name = 'piscineds'

file = './subject/item/item.csv'
table = 'item_1'

connection = f'postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'
engine = create_engine(connection)

# leer el fichero
df = pd.read_csv(file)

# comprobacion de los datos
# print(df.head())

# Filtrar las filas donde `category_id`, `category_code` y `brand` NO estén todas vacías
filtered_df = df.dropna(
    subset=['category_id', 'category_code', 'brand'], how='all')

# Comprobación de los datos filtrados
print("\nDatos después de filtrar filas vacías (excepto product_id):")
print(filtered_df.head())


filtered_df.to_sql(table, engine, if_exists='replace', index=False)

print(f"Los datos se han importado correctamente en la tabla {table}.")
