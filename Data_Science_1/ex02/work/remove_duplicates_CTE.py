import os
import time
import pandas as pd
from tqdm import tqdm
from sqlalchemy import create_engine, text

db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_user = os.getenv('DB_USER')
db_pass = os.getenv('DB_PASS')
db_name = os.getenv('DB_NAME')

connection = f'postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'
engine = create_engine(connection)

table = "cop_cust"

query = f"""
WITH cte AS (
    SELECT ctid, ROW_NUMBER() OVER (
        PARTITION BY event_type, product_id
        ORDER BY event_time
    ) as rn
    FROM {table}
)
DELETE FROM customers
WHERE ctid IN (
    SELECT ctid
    FROM cte
    WHERE rn > 1
);
"""


# Crear tabla temporal para almacenar los datos limpios
try:

    start_time = time.time()
    print("Iniciando la eliminación de duplicados...")

    with engine.connect() as conn, conn.begin():
        conn.execute(text(query))

    elapsed_time = time.time() - start_time
    print(f"Eliminación de duplicados completada en {
          elapsed_time:.2f} segundos.")


except Exception as e:
    print(f"Error  '{table}': {e}")


# 1747.49 segundos. 29 minutos
