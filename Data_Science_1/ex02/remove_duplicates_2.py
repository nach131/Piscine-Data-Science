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
    SELECT ctid
    FROM (
        SELECT
        ctid,
        ROW_NUMBER() OVER (PARTITION BY user_id, event_time, user_session, product_id, price, event_type ORDER BY ctid) AS row_num
        FROM
        {table}
    ) subquery
    WHERE row_num > 1
    )
    DELETE FROM {table}
    USING duplicates
    WHERE {table}.ctid = duplicates.ctid;
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


# DELETE 643708
# registros 11627698

# Query returned successfully in 3 min 7 secs.
