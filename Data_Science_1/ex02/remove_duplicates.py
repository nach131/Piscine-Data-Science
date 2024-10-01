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
    WITH duplicates AS (
        SELECT
            ctid,  -- ctid se usa para identificar filas únicas en PostgreSQL
            event_time,
            event_type,
            product_id,
            LEAD(event_time) OVER (PARTITION BY event_type, product_id ORDER BY event_time) AS next_event_time
        FROM
            {table}
    )
    DELETE FROM {table}
    USING duplicates
    WHERE
        {table}.ctid = duplicates.ctid
        AND duplicates.next_event_time IS NOT NULL  -- Asegurar que haya un siguiente evento
        AND duplicates.event_type = {table}.event_type
        AND duplicates.product_id = {table}.product_id
        AND EXTRACT(EPOCH FROM (duplicates.next_event_time - duplicates.event_time)) <= 1;
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


# Eliminación de duplicados completada en 147.88 segundos.  2,4 minutos
