import os
import time
from sqlalchemy import create_engine, text

db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_user = os.getenv('DB_USER')
db_pass = os.getenv('DB_PASS')
db_name = os.getenv('DB_NAME')

connection = f'postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'
engine = create_engine(connection)

table = "customers"

query = f"""
    DELETE FROM {table} a
    USING {table} b
    WHERE a.ctid < b.ctid
    AND a.event_type = b.event_type
    AND a.product_id = b.product_id
    AND ABS(EXTRACT(EPOCH FROM a.event_time) - EXTRACT(EPOCH FROM b.event_time)) < 1;
"""

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
