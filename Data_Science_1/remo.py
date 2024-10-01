import os
import time
from tqdm import tqdm
from sqlalchemy import create_engine, text

db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_user = os.getenv('DB_USER')
db_pass = os.getenv('DB_PASS')
db_name = os.getenv('DB_NAME')

connection = f'postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'
engine = create_engine(connection)

table = "tomate"
tmp_table = "tmp"


# Parámetros de chunking
# Número de filas por chunk (ajustar según memoria disponible)
chunksize = 1000
offset = 0

# Crear tabla temporal para almacenar los datos limpios
try:
    with engine.connect() as conn, conn.begin():
        # Elimina la tabla temporal si ya existe
        conn.execute(f"DROP TABLE IF EXISTS {tmp_table};")
        # Crea una tabla temporal vacía con la misma estructura
        conn.execute(f"CREATE TABLE {tmp_table} (LIKE {table} INCLUDING ALL);")

except Exception as e:
    print(f"Error creating table '{tmp_table}': {e}")
