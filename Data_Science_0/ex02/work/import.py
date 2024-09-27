import pandas as pd
from sqlalchemy import create_engine

db_user = 'nmota-bu'
db_pass = 'mysecretpassword'
db_host = 'db'
db_port = '5432'
db_name = 'piscineds'

file = './customer/data_2022_dec.csv'

connection = f'postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'
engine = create_engine(connection)

# leer el fichero
df = pd.read_csv(file)

# comprobacion de los datos
# print(df.head())

table_name = "data_2022_dec"
df.to_sql(table_name, engine, if_exists='replace', index=False)

print(f"Los datos se han importado correctamente en la tabla {table_name}.")
