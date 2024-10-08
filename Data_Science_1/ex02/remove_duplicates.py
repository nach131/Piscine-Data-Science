import os
import pandas as pd
from sqlalchemy import create_engine, text

# Parámetros de conexión
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_user = os.getenv('DB_USER')
db_pass = os.getenv('DB_PASS')
db_name = os.getenv('DB_NAME')


# Crear la conexión a la base de datos
connection = f'postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'
engine = create_engine(connection)

# Tabla a procesar
table = "customers"              # Tabla original
new_table_name = "cleaned_customers"
last_record = None

# Leer datos de la tabla en chunks para evitar problemas de memoria
chunk_size = 10000  # Ajustar según el tamaño de la tabla y la memoria disponible
count = 0
count_del_duplicates = 0
count_del_time = 0

with engine.connect() as conn:
    for chunk in pd.read_sql_table(table, con=conn, chunksize=chunk_size):
        # Ordenar cada fragmento por 'event_time'
        chunk = chunk.sort_values('event_time')

        # Contar el número de registros antes de eliminar duplicados
        before_dedup_count = chunk.shape[0]
        # Eliminar duplicados dentro del fragmento actual
        clean_chunk = chunk.drop_duplicates()
        # Contar el número de registros después de eliminar duplicados
        after_dedup_count = clean_chunk.shape[0]

        # Calcular el número de duplicados eliminados y acumular el total
        count_del_duplicates += (before_dedup_count - after_dedup_count)

        if last_record is not None and not clean_chunk.empty:
            # Inicializar con el último registro del chunk anterior
            filtered_chunk = [last_record]

            for index, row in clean_chunk.iterrows():
                # Calcular la diferencia de tiempo con el último registro guardado
                time_diff = abs(pd.Timestamp(
                    filtered_chunk[-1]['event_time']) - pd.Timestamp(row['event_time'])).total_seconds()

                # Si la diferencia de tiempo es mayor a 1 segundo o el `event_type` y
                # `product_id` no coinciden, agregar el registro a `filtered_chunk`
                if time_diff > 1 or filtered_chunk[-1]['event_type'] != row['event_type'] or filtered_chunk[-1]['product_id'] != row['product_id']:
                    filtered_chunk.append(row)
                else:
                    # Si no, eliminarlo y contar la eliminación
                    count_del_time += 1

            # Crear un nuevo DataFrame con los registros filtrados
            clean_chunk = pd.DataFrame(filtered_chunk)

            # Si hay datos después de la eliminación, procesarlos
        if not clean_chunk.empty:
            if count == 0:
                # Crear la tabla con el primer fragmento limpio
                clean_chunk.to_sql(new_table_name, con=engine,
                                   if_exists='replace', index=False)
            else:
                # Insertar el fragmento limpio en la tabla
                clean_chunk.to_sql(new_table_name, con=engine,
                                   if_exists='append', index=False)

            # Actualizar `last_record` al último registro del `clean_chunk`
            last_record = clean_chunk.iloc[-1]

        # Aumentar el contador de fragmentos y mostrar el progreso
        count += 1
        print(f"Fragmento procesado: {count}", end='\r')

print(f"\nRegistros eliminados por drop_duplicates: {count_del_duplicates}")
print(f"Registros eliminados por diferencia de tiempo < 1 segundo: {
      count_del_time}")

# Fragmento procesado: 1228
# Registros eliminados por drop_duplicates: 643605
# Registros eliminados por diferencia de tiempo < 1 segundo: 56381
