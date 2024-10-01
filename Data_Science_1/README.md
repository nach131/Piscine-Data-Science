# Piscine-Data-Science


# Contar
SELECT COUNT(*) FROM data_2022_dec;

| | |
| -- | -- |
| data_2022_dec | 3.533.286 |
| data_2022_nov | 4.635.837 |
| data_2022_Oct | 4.102.283 |
| | |
| customers | 12.271.406 |

DESPUES DE BORRAR DUPLICADOS
| customers | 11.363.281 |


# Contar y sumar los registro de varias tablas

	SELECT
		(SELECT COUNT(*) FROM data_2022_dec) AS total_tabla1,
		(SELECT COUNT(*) FROM data_2022_nov) AS total_tabla2,
		(SELECT COUNT(*) FROM data_2022_Oct) AS total_tabla3,
		(SELECT COUNT(*) FROM data_2022_dec) + 
		(SELECT COUNT(*) FROM data_2022_nov) + 
		(SELECT COUNT(*) FROM data_2022_Oct) AS total_registros;

# Consultar fila con unda condicion
SELECT COUNT(*) FROM nombre_de_la_tabla WHERE columna = 'valor';


## UNION
	CREATE TABLE customers AS
	SELECT * FROM data_2022_dec
	UNION ALL
	SELECT * FROM data_2022_nov
	UNION ALL
	SELECT * FROM data_2022_oct


# Copiar la estructura de la tabla (sin datos)
	CREATE TABLE nueva_tabla AS
	SELECT *
	FROM tabla_original
	WHERE 1 = 0;

# en PostgreSQL
CREATE TABLE nueva_tabla (LIKE tabla_original INCLUDING ALL);


# Copiar la estructura y los datos

	CREATE TABLE nueva_tabla AS
	SELECT *
	FROM tabla_original;

# Buscar y borrar duplicados

	DELETE FROM {table} a
	USING {table} b
	WHERE a.ctid < b.ctid
	AND a.event_type = b.event_type
	AND a.product_id = b.product_id
	AND ABS(EXTRACT(EPOCH FROM a.event_time) - EXTRACT(EPOCH FROM b.event_time)) < 1;

# Borrar tabla
	DROP TABLE cp_cust;




Después de realizar grandes operaciones de eliminación en PostgreSQL, el uso de VACUUM ayuda a liberar espacio y a evitar problemas de rendimiento. También se recomienda ejecutar ANALYZE para actualizar las estadísticas de la base de datos:


    VACUUM FULL customers;
    ANALYZE customers;

