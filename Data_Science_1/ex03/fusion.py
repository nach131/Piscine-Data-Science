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
item = "item"

query = f"""
    ALTER TABLE {table}
    ADD COLUMN category_id BIGINT,
    ADD COLUMN category_code VARCHAR(255),
    ADD COLUMN brand VARCHAR(255);

    UPDATE {table} c
    SET
        category_id = i.category_id,
        category_code = i.category_code,
        brand = i.brand
    FROM {item} i
    WHERE c.product_id = i.product_id;
"""

try:

    start_time = time.time()
    print("Iniciando fusion...")

    with engine.connect() as conn, conn.begin():
        conn.execute(text(query))

    elapsed_time = time.time() - start_time
    print(f"Fusion completada en {elapsed_time:.2f} segundos.")


except Exception as e:
    print(f"Error  '{table}': {e}")

# Fusion completada en 127.22 segundos.
