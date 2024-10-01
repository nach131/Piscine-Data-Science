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

final_table = "customers"

with engine.connect() as conn:
    # print("Connect")
    result = conn.execute(text("""
    SELECT table_name
    FROM information_schema.tables
    WHERE table_name LIKE 'data_2022%'
    """))
    table_names = [row[0] for row in result]
    print(table_names)

# Construir la consulata de UNION

union = f"CREATE TABLE {final_table} AS \n"
union += "\nUNION ALL\n".join(
    [f"SELECT * FROM {table}" for table in table_names])

print(union)

# ejecutar la consulta de union
try:
    with engine.connect() as conn, conn.begin():
        startTime = time.time()

        conn.execute(text(union))

        print(f"\n\t[-- TIME --] {time.time() - startTime:.2f} sec\n")
        print(f"All tables have been successfully joined in '{final_table}'.")

except Exception as e:
    print(f"Error creating table '{final_table}': {e}")


# CREATE TABLE customers AS
# SELECT * FROM data_2022_dec
# UNION ALL
# SELECT * FROM data_2022_nov
# UNION ALL
# SELECT * FROM data_2022_oct
