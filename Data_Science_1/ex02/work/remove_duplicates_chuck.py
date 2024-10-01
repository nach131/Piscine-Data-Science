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
        DO $$
        DECLARE
            chunk_size INT := 1000;  -- Tamaño del chunk
            rows_deleted INT;
        BEGIN
            LOOP
                WITH cte AS (
                    SELECT a.ctid
                    FROM {table} a
                    JOIN {table} b ON a.event_type = b.event_type
                            AND a.product_id = b.product_id
                            AND a.ctid < b.ctid
                            AND ABS(EXTRACT(EPOCH FROM a.event_time) - EXTRACT(EPOCH FROM b.event_time)) < 1
                    LIMIT chunk_size
                    FOR UPDATE
                )
                DELETE FROM {table}
                WHERE ctid IN (SELECT ctid FROM cte);

                GET DIAGNOSTICS rows_deleted = ROW_COUNT;

                -- Salir del bucle si no se eliminaron filas
                EXIT WHEN rows_deleted = 0;

            END LOOP;
        END $$;
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
