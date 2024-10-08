import os
import pandas as pd
from sqlalchemy import create_engine, text
import time

# Parámetros de conexión (ajusta según tus variables de entorno)
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_user = os.getenv('DB_USER')
db_pass = os.getenv('DB_PASS')
db_name = os.getenv('DB_NAME')

# Crear la conexión a la base de datos
connection = f'postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'
engine = create_engine(connection)

# Nombre de las tablas
table = "customers"
item_table = "item"
# Nueva tabla donde se guardará el resultado
new_table_name = "customers_with_categories"

# Tamaño del chunk
chunk_size = 10000  # Ajusta este valor según la memoria disponible

try:
    start_time = time.time()
    print("Iniciando fusión...")

    # Cargar la tabla item completamente en un DataFrame
    item_df = pd.read_sql_table(item_table, con=engine)

    chunk_count = 0

    # Leer el item en fragmentos y actualizar la tabla customers
    with engine.connect() as conn:
        for chunk in pd.read_sql_table(table, con=conn, chunksize=chunk_size):
            # Fusionar el chunk actual de customers con item_df
            merged_chunk = pd.merge(
                chunk, item_df, on='product_id', how='left')

            # Guardar el chunk fusionado en la nueva tabla
            if chunk_count == 0:
                merged_chunk.to_sql(new_table_name, con=engine,
                                    if_exists='replace', index=False)
            else:
                merged_chunk.to_sql(new_table_name, con=engine,
                                    if_exists='append', index=False)

            # Aumentar el contador de chunks procesados
            chunk_count += 1
            print(f"Fragmento procesado: {chunk_count}", end='\r')

    elapsed_time = time.time() - start_time
    print(f"Fusión completada en {elapsed_time:.2f} segundos.")

except Exception as e:
    print(f"Error en la fusión de '{table}': {e}")
